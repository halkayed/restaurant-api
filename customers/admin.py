from django.contrib import admin

from .models import Customer, Menu, Item
# Register your models here.
admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Item)