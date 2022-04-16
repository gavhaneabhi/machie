from email import message
from multiprocessing import AuthenticationError
from pyexpat.errors import messages
from re import U
from telnetlib import AUTHENTICATION
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib import admin


# Create your views here. 
def index(request):
    return render(request, 'index.html')

def login(request):

    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(request, username = username, password = password)

       if user is not None:
           auth.login(request, user)        
           return redirect(request, "results.html")

       else:
            message.info(request, 'invalid credentials')                   

    else:
        return render(request, 'index.html') 
        
def results(request):
    return render(request, 'results.html')   

def graph(request):
    return render(request, 'graph.html')   


    

    
    
    

