from django import forms
from django.shortcuts import render
from requests import request
from django import forms
from django.http import HttpResponseRedirect


class LoginForm(forms.Form):
    username = forms.CharField(label='username',max_length=10)
    password = forms.PasswordInput()
    
    
def login(request):
    if request.method == "POST":
        
        form = LoginForm(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect("/blog/templates/blog/index.html")
        
        else:
            form = LoginForm()
    
    return render(request,'blogdaily/index.html',{'form':form})