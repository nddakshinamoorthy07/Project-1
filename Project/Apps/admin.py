from django.contrib import admin
from .models import Role, User, Kitchen, Brand, MenuItem, Order, Payment, InventoryItem, StaffAssignment



@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'email', 'role')
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name', 'email')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_full_name.short_description = 'Full Name' 


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('name', 'location')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


from .models import Tag
@admin.register(Tag) 
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'price', 'is_available')
    list_filter = ('brand', 'is_available')
    search_fields = ('name',)
    filter_horizontal = ('tags',)


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit', 'reorder_threshold')
    search_fields = ('name', 'unit')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total_amount', 'payment_status', 'order_time')
    list_filter = ('status', 'payment_status')
    search_fields = ('customer__name',)
    autocomplete_fields = ('customer', 'delivery_staff', 'brand', 'kitchen')


@admin.register(StaffAssignment)
class StaffAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'kitchen', 'skill', 'shift_start', 'shift_end')
    list_filter = ('skill', 'kitchen')
    autocomplete_fields = ('user', 'kitchen')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'payment_method', 'amount', 'service_charge', 'payment_time')
    list_filter = ('payment_method',)
    autocomplete_fields = ('order',)


from .models import Notification
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read')

