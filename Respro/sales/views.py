from django.shortcuts import render
from .models import SalesReport

def sales_report_view(request):
    reports = SalesReport.objects.all()
    return render(request, 'sales/report.html', {'reports': reports})
