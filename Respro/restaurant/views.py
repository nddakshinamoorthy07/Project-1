from django.shortcuts import render
from .models import Restaurant, Table

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/list.html', {'restaurants': restaurants})
