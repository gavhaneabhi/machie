from email import message
from pyexpat.errors import messages
from re import U
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import admin


# Create your views here. 
def index(request):
    return render(request, 'index.html')

def login(request):

    if request.method == 'POST':
       U = User.objects.get(usename='Abhishek')
       U.set_passward(12345)
       U.save()

    user = authenticate(username = 'Abhishek', password = '12345')

    if user is not None:
        login(request, user)
        return redirect(request, "results.html")
        

    else:
        messages.error(request, "Invalid userID or Passward")
        return redirect('index.html') 
        
def results(request):
    return render(request, 'results.html')   

    

    
    
    

