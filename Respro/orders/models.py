# orders/models.py

from django.db import models
from django.contrib.auth.models import User  # or your custom user

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # other fields...

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # other fields...
