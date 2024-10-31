import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm


def index(request):
    # Получаем путь к папке с изображениями
    pictures_dir = os.path.join(settings.MEDIA_ROOT, 'pictures')

    # Получаем список всех файлов в папке pictures
    images = []
    if os.path.exists(pictures_dir):
        images = [f'pictures/{img}' for img in os.listdir(pictures_dir) if img.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    return render(request, 'index.html', {'images': images})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'profile.html')
