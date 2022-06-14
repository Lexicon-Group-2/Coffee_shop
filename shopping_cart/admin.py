from django.contrib import admin
from .models import Customer, Order, OrderItem, ShippingAddress

class CustomerAdmin(admin.ModelAdmin):
    list_display  = ('first_name', 'last_name', 'id')
    search_fields = ['first_name',]

class OrderAdmin(admin.ModelAdmin):
    list_display  = ('id', 'date_ordered', 'completed')
    search_fields = ['complete',]

class OrderItemAdmin(admin.ModelAdmin):
    list_display  = ('order', 'product', 'quantity')
    search_fields = ['order',]

class ShippingAddressItemAdmin(admin.ModelAdmin):
    list_display  = ('customer', 'order', 'address')
    search_fields = ['customer',]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressItemAdmin)

