from django.db import models
from restaurant.models import Restaurant

class Transaction(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('upi', 'UPI'),
        ('wallet', 'Wallet'),
    ]

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.restaurant.name} - ₹{self.amount} on {self.date.strftime('%Y-%m-%d')}"

class SalesReport(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    report_date = models.DateField()
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)
    transactions_count = models.PositiveIntegerField()

    def __str__(self):
        return f"Sales Report for {self.restaurant.name} on {self.report_date}"
