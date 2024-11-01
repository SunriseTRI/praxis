from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('profile/', user_profile_view, name='user_profile'),
    # path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
    # path('profile/book-session/', views.book_session, name='book_session'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

