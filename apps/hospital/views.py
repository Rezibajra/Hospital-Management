from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def signup_page(request):
    return render(request, 'hospital/signup.html')

def home(request):
    return render(request, 'hospital/home.html')

def login_page(request):
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password doesn't exist.")
    return render(request, 'hospital/login.html')

def logout_page(request):
    logout(request)
    return redirect('home')


