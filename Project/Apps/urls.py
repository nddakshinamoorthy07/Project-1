from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.orders, name='orders'),
    path('kitchens/', views.kitchens, name='kitchens'),
    path('brands/', views.brands, name='brands'),
    path('payments/', views.payments, name='payments'),
    path('menu/', views.menu, name='menu'),
    path('inventory/', views.inventory, name='inventory'),
    path('staff/', views.staff, name='staff'),
    path('login/', views.login_view, name='login'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/staff/', views.staff_dashboard, name='staff_dashboard'),
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),
]
