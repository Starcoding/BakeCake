from django.contrib import admin
from .models import Component, CustomUser, Order, Product

admin.site.register(Component)
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Order)

# Register your models here.

