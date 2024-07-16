from django.contrib import admin
from .models import Category,Item
# Register your models here.

# to show the database on the django admin site
admin.site.register(Category)
admin.site.register(Item)

