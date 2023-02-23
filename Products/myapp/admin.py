from django.contrib import admin
from .models import product_mst

# Register your models here.
class product_mstAdmin(admin.ModelAdmin):
    list_display=['productname']

    admin.site.register(product_mst)