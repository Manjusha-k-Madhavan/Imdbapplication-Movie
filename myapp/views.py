from django.shortcuts import render,redirect


from django.views.generic import View
from myapp.models import Movie

from django import forms
class MovieForm(forms.Form):
    name=forms.CharField()
    language=forms.CharField()
    run_time=forms.IntegerField()
    genre=forms.CharField()
    director=forms.CharField()
    year=forms.IntegerField()
    actors=forms.CharField()



class MovieListView(View):
    def get(self,request,*args,**kwargs):
        qs=Movie.objects.all()
        return render(request,"movie_list.html",{"data":qs})


class MovieDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        return render(request,"movie_detail.html",{"data":qs})
    

class MovieDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        return redirect("movie-list")
    
class MovieCreateView(View):
    def get(self,request,*args,**kwargs):
        form=MovieForm()
        return render(request,"movie_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=MovieForm(request.POST)      #defcleaned is working with reques.post
        if form.is_valid():                 #check errors
            data=form.cleaned_data
            Movie.objects.create(**data)
            return redirect("movie-list")
        else:
            return render(request,"movie_add.html",{"form":form})



        # print(request.POST)
        # return redirect("movie-list")
        
        # we want to unpack
        #dict={key:value,key:value}
        # **dict key=value,key=value

        # request.POST.pop("csrfmiddlewaretoken")

        # the unsterd one to stred by k,v


        # data={k:v for k,v in request.POST.items()}
        # print(data)
        # data.pop("csrfmiddlewaretoken")
        # Movie.objects.create(**data)
        # return redirect("movie-list")


#url:lh:8000/movies/{id}/change/
class MovieUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie_object=Movie.objects.get(id=id)
        data={
            "name": movie_object.name,
            "language": movie_object.language,
            "run_time": movie_object.run_time,
            "genre": movie_object.genre,
            "director": movie_object.director,
            "year": movie_object.year,
            "actors": movie_object.actors

        }
        form=MovieForm(initial=data)
        return render(request,"movie_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=MovieForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            id=kwargs.get("pk")
            Movie.objects.filter(id=id).update(**data)
            return redirect("movie-list")
        else:
            return render(request,"movie_edit.html",{"form":form})
        
         # data={k:v for k,v in request.POST.items()}
        # data.pop("csrfmiddlewaretoken")
        # id=kwargs.get("pk")
        # Movie.objects.filter(id=id).update(**data)
        # return redirect("movie-list")


    


    

    
    

