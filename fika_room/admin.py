from django.contrib import admin
from .models import ChatPost


class ChatPostAdmin(admin.ModelAdmin):
    list_display  = ('user', 'date_added', 'content')
    search_fields = ['user',]

admin.site.register(ChatPost, ChatPostAdmin)
