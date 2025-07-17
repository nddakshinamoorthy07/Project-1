from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role_id = models.IntegerField()

class Kitchen(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class KitchenBrand(models.Model):
    kitchen_id = models.IntegerField()
    brand_id = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=255)
    brand_id = models.IntegerField()

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.IntegerField()
    brand_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=255)
    is_available = models.BooleanField()

class KitchenMenuAvailability(models.Model):
    kitchen_id = models.IntegerField()
    menu_item_id = models.IntegerField()
    is_available = models.BooleanField()

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)
    reorder_threshold = models.IntegerField()

class KitchenInventory(models.Model):
    kitchen_id = models.IntegerField()
    inventory_item_id = models.IntegerField()
    quantity_available = models.FloatField()

class InventoryUsage(models.Model):
    order_id = models.IntegerField()
    inventory_item_id = models.IntegerField()
    quantity_used = models.FloatField()

class Order(models.Model):
    customer_id = models.IntegerField()
    brand_id = models.IntegerField()
    kitchen_id = models.IntegerField()
    status = models.CharField(max_length=50)
    order_time = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50)
    delivery_staff_id = models.IntegerField(null=True, blank=True)

class OrderItem(models.Model):
    order_id = models.IntegerField()
    menu_item_id = models.IntegerField()
    quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

class ItemAddon(models.Model):
    menu_item_id = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class OrderItemAddon(models.Model):
    order_item_id = models.IntegerField()
    addon_id = models.IntegerField()
    addon_price = models.DecimalField(max_digits=10, decimal_places=2)

class StaffAssignment(models.Model):
    user_id = models.IntegerField()
    kitchen_id = models.IntegerField()
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    skill = models.CharField(max_length=255)

class Payment(models.Model):
    order_id = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    payment_time = models.DateTimeField()

class OrderCancellation(models.Model):
    order_id = models.IntegerField()
    cancelled_by_id = models.IntegerField()
    reason = models.TextField()
    cancelled_at = models.DateTimeField()

class Notification(models.Model):
    user_id = models.IntegerField()
    order_id = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
