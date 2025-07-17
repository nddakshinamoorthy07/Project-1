from django.db import models
from django.contrib.auth.models import User

# Restaurant model
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# Table model
class Table(models.Model):
    table_number = models.IntegerField()
    seats = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Table {self.table_number} at {self.restaurant.name}"

# MenuItem model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

# Reservation model (optional)
class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()

    def __str__(self):
        return f"Reservation by {self.customer.username} for Table {self.table.table_number}"
