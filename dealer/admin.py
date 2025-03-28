from django.contrib import admin

from dealer.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'description', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk' , 'category_name')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product',  'version_number', 'version_name', 'is_active')
