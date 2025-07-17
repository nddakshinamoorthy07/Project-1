from django.contrib import admin
from .models import Transaction, SalesReport

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount', 'payment_method', 'timestamp')
    list_filter = ('payment_method',)
    search_fields = ('order__id',)

@admin.register(SalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'report_date', 'total_sales')
    list_filter = ('report_date',)
