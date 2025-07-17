from django.shortcuts import render
from .models import Stock

def stock_list(request):
    stock_items = Stock.objects.all()
    return render(request, 'inventory/stock_list.html', {'stock_items': stock_items})
