from django.contrib import admin
from .models import Restaurant, Table

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'manager')
    search_fields = ('name', 'location')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity', 'restaurant')
    list_filter = ('restaurant',)
