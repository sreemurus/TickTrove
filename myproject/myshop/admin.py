from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from myshop.models import Product, Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'price']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username']


class UserAdmin(BaseUserAdmin):
    pass



