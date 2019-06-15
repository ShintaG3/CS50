from django.contrib import admin
from django.db import models
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product

class VariationAdmin(admin.ModelAdmin):
    list_display = ['_products', 'category', '__str__', 'price']

    def _products(self, row):
        return ','.join([x.title for x in row.products.all()])


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)


# Register your models here.
