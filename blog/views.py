from django.shortcuts import render
from .models import *


def home(request):
    
    context = {
        
    }
    
    return render(request,'pages/home.html',context)


def about(request):
    
    context = {
        
    }
    
    return render(request,'pages/about.html',context)


def contact(request):
    
    context = {
        
    }
    
    return render(request,'pages/contact.html',context)


def post(request,pk):
    
    context = {
        
    }
    
    return render(request,'pages/post.html',context)