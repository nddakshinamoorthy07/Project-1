from django.contrib import admin
from .models import Kitchen

@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')