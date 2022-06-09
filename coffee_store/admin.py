from django.contrib import admin
from .models import CoffeeMachine, CoffeeBeans, CoffeeMugs, Accessory


class CoffeeMachineAdmin(admin.ModelAdmin):
    list_display  = ('title', 'price', 'id')
    search_fields = ['title',]


# Register your models here.
admin.site.register(CoffeeMachine, CoffeeMachineAdmin)
admin.site.register(CoffeeBeans)
admin.site.register(CoffeeMugs)
admin.site.register(Accessory)
