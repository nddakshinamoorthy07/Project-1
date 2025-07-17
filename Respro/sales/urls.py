from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.sales_report_view, name='sales-report'),
]
