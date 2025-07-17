from django.contrib import admin
from .models import (
    Role, User, Kitchen, Brand, KitchenBrand, Category, MenuItem,
    KitchenMenuAvailability, InventoryItem, KitchenInventory,
    InventoryUsage, Order, OrderItem, ItemAddon, OrderItemAddon,
    StaffAssignment, Payment, OrderCancellation, Notification
)

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Kitchen)
admin.site.register(Brand)
admin.site.register(KitchenBrand)
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(KitchenMenuAvailability)
admin.site.register(InventoryItem)
admin.site.register(KitchenInventory)
admin.site.register(InventoryUsage)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ItemAddon)
admin.site.register(OrderItemAddon)
admin.site.register(StaffAssignment)
admin.site.register(Payment)
admin.site.register(OrderCancellation)
admin.site.register(Notification)
