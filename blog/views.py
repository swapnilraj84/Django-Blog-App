from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User

# Create your views here.

def testing(request):
    return render(request, 'blog/base.html')

def login(request):
    return render(request, 'blog/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST('uname')
        email = request.POST('uemail')
        password = request.POST('upassword')
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
    return render(request, 'blog/signup.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
