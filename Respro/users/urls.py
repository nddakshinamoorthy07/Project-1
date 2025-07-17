# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='users_home'),
    path('profiles/', views.list_profiles, name='profile_list'),
]
