from django.contrib import admin
from .models import book

# Register your models here.

class bookuser(admin.ModelAdmin):
    list_display=['Bookname','Title','Author','Isbn','Publisher']

admin.site.register(book)
