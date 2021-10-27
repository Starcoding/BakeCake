from django.contrib import admin
from .models import Component, CustomUser, Order

admin.site.register(Component)
admin.site.register(CustomUser)
admin.site.register(Order)

# Register your models here.
