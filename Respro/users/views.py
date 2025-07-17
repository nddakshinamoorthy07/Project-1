# users/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile

def home(request):
    return HttpResponse("Users app is working")

def list_profiles(request):
    profiles = Profile.objects.select_related('user').all()
    return render(request, 'users/profile_list.html', {'profiles': profiles})
