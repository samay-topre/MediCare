from django.contrib import admin
from .models import Product, Cart, CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'image']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']
