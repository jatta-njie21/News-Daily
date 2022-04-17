from django.shortcuts import render
from requests import request
from . import models

# Create your views here.


def get_object():
    test = models.Post.objects.all()
    return test

def index(request):
    return render(request,'blog/index.html',{
        "posts": get_object()
    })
    
def authors(request):
    return render(request,'blog/authors.html')
    
def details(request,blog_id):
    item = models.Post.objects.get(pk = blog_id)
    return render(request,'blog/details.html',{
        "items": item
    })