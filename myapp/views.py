import os
from django.conf import settings
from django.shortcuts import render

def index(request):
    # Получаем путь к папке с изображениями
    pictures_dir = os.path.join(settings.MEDIA_ROOT, 'pictures')

    # Получаем список всех файлов в папке pictures
    images = []
    if os.path.exists(pictures_dir):
        images = [f'pictures/{img}' for img in os.listdir(pictures_dir) if img.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    return render(request, 'index.html', {'images': images})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Session
from .forms import UserProfileForm, SessionBookingForm

@login_required
def user_profile(request):
    user_sessions = request.user.sessions.all().order_by('-date')[:5]  # Get last 5 sessions
    return render(request, 'user_profile.html', {'user_sessions': user_sessions})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def book_session(request):
    if request.method == 'POST':
        form = SessionBookingForm(request.POST)
        if form.is_valid():
            session = Session(
                name="New Session",
                date=form.cleaned_data['session_date'],
                user=request.user
            )
            session.save()
            return redirect('user_profile')
    else:
        form = SessionBookingForm()
    return render(request, 'book_session.html', {'form': form})