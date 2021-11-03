from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin
from .models import Component, CustomUser, Order, Product

admin.site.register(Component)
admin.site.register(CustomUser)
admin.site.register(Product)
# admin.site.register(Order)

# Register your models here.

class OrderResourse(resources.ModelResource):

    class Meta:
        model = Order


class OrderAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    resource_class = OrderResourse
    list_filter = ('status', )


admin.site.register(Order, OrderAdmin)