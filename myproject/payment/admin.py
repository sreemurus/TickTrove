

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'created_at')
    list_filter = ('user',)
    search_fields = ('id', 'user__username')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    list_filter = ('order__user',)
    search_fields = ('order__id', 'product__name')
