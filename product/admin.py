from django.contrib import admin
from product import models as product_models


@admin.register(product_models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'brand', 'category', 'ratings', 'stock', 'user', 'createdAt')
    search_fields = ('name', 'description', 'brand', 'category')
    list_filter = ('category', 'ratings', 'stock', 'createdAt')
    date_hierarchy = 'createdAt'
    ordering = ('-createdAt',)
    readonly_fields = ('createdAt',)
    