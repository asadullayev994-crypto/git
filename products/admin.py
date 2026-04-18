from django.contrib import admin
from .models import Product, Order, PromoCode


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'active', 'expires_at', 'created_at')
    list_filter = ('active',)
    search_fields = ('code',)