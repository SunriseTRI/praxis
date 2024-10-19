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