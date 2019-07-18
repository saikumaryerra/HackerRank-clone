from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def signup(request):
    form=SignUpForm()
    return render(request, 'registration/signup.html', {'form':form}) 

def login(request):
    return render(request, 'registration/login.html', {})