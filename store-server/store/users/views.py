from django.shortcuts import render

from users.models import User
from users.forms import UserLoginForm

def login(request):
    context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context)

def registration(request):
    return render(request, 'users/registration.html')
