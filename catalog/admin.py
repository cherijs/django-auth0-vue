from django.contrib import admin

# Register your models here.
from catalog.models import Product

admin.site.site_header = 'SLUT'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'description', 'buyPrice', 'sellPrice', 'unit', 'quantity')
