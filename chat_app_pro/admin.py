from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'content', 'timestamp', 'received', 'read')
    list_filter = ('from_user', 'to_user', 'received', 'read')
    search_fields = ('from_user__username', 'to_user__username', 'content')


admin.site.register(Message, MessageAdmin)
