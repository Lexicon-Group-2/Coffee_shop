from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('name', 'id')
    search_fields = ['name',]

class ProductAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'image1', 'price', 'id')
    search_fields = ['title',]

# Register your models here.
#admin.site.register(CoffeeMachine, CoffeeMachineAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
