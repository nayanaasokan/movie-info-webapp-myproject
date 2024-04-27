from django.shortcuts import render,redirect
from myapp.models import Movie
from django.views.generic import View
from myapp.forms import MovieForm


# Create your views here.

# views for listing all movies
# url: localhost:8000/movies/all
# method:get()

# def movie_list_view(request,*args,**kwargs):
#     qs=Movie.objects.all()
#     return render(request,"movie_list.html",{"data":qs})

class MovieListView(View):
    def get(self,request,*args,**kwargs):
        qs=Movie.objects.all()
        return render(request,"movie_list.html",{"data":qs})
    
# View for creating movie
# url:localhost:8000/myapp/movies/add/
# method:post,get
class MovieCreateView(View):
     def get(self,request,*args,**kwargs):
         form=MovieForm()
         return render(request,"movie_add.html",{"form":form})
     def post(self,request,*args,**kwargs):
         form=MovieForm(request.POST,files=request.FILES)
         if form.is_valid():
             data=form.cleaned_data
             Movie.objects.create(**data)
             return redirect("movie-list")
         return render(request,"movie_add.html",{"form":form})

# to get details of a particular movie 
#url:localhost:8000/myapp/movies/{id}
# method:get()
class MovieDetailView(View):
    def get(self,request,*args,**kwargs):
        id=3
        qs=Movie.objects.get(id=id)
        return render(request,"movie_detail.html",{"data":qs})
    

# To get details of any specific movie
class MovieDetailView(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)    #kwargs={"pk":6}
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        return render(request,"movie_detail.html",{"data":qs})           

# To delete  a particular movie detail
# url-localhost:8000/myapp/movies/{id}/remove 
# method-get
    
class MovieDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        return redirect("movie-list")
    
# To update
    # url:localhost:8000/myapp/movies/{id}/change/
    # method:get,post

class MovieUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie_object=Movie.objects.get(id=id)
        form=MovieForm(instance=movie_object)   #to initialize, here we use instance. it is applicable only for modelform.
        return render(request,"movie_update.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie_object=Movie.objects.get(id=id)
        form=MovieForm(request.POST,instance=movie_object,files=request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('movie-list')
        else:
            return render(request,"movie_update.html",{"form":form})
        
