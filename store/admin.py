from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Customer, Product, Order, OrderItem, ShippingAddress


@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    pass


@admin.register(ShippingAddress)
class ShippingAddressAdmin(ModelAdmin):
    pass
