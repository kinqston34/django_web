import posts


# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Location, Post
def index(request):
    posts = Post.objects.all()
    #SELECT * FROM posts_post
    #return HttpResponse("My First Django App.")
    #posts = Post.objects.filter(location = '3')
    return render(request,"index.html",{"posts": posts})