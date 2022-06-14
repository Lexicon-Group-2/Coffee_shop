from django.contrib import admin
from .models import ChatPost


class ChatPostAdmin(admin.ModelAdmin):
    list_display  = ('user', 'content', 'date_added')
    search_fields = ['user',]

admin.site.register(ChatPost, ChatPostAdmin)
