from django.db import models

# === Master Data ===
# users/models.py


class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    username = models.CharField(max_length=255, default='default_username',unique=True)

    REQUIRED_FIELDS = ['email'] 

    def __str__(self):
        return self.username



class Kitchen(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tag, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)
    reorder_threshold = models.IntegerField()

    def __str__(self):
        return self.name

# === Choices for statuses ===

ORDER_STATUS = [
    ('pending', 'Pending'),
    ('preparing', 'Preparing'),
    ('ready', 'Ready'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
]

PAYMENT_STATUS = [
    ('pending', 'Pending'),
    ('paid', 'Paid'),
    ('failed', 'Failed'),
]

PAYMENT_METHODS = [
    ('cash', 'Cash'),
    ('card', 'Card'),
    ('upi', 'UPI'),
    ('wallet', 'Wallet'),
]

# === Transaction Models ===

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS, default='pending')
    order_time = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS, default='pending')
    delivery_staff = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="deliveries")

    def __str__(self):
        return f"Order #{self.id} by {self.customer}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS, default='cash')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.id} for Order #{self.order.id}"

# === Staffing ===

class StaffAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=True, blank=True)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    skill = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user} @ {self.kitchen} [{self.shift_start} - {self.shift_end}]"

# === Notifications ===


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # <-- This fixes your error

    def __str__(self):
        return f"To {self.user.username}: {self.message[:30]}"


# models.py
class Staff(models.Model):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)  # e.g., Waiter, Chef, Cleaner
    contact = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.role}"
