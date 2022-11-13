from django.shortcuts import render, redirect
from django.contrib.auth import logout,login,authenticate
# Create your views here.


def register_req(request):
    return render(request,'acc/register.html')



def login_req(request):
    return render(request,'acc/login.html')



def logout_req(request):
    logout(request)
    return redirect ('login')