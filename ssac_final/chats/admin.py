from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from chats.models import Message
from . import models
@admin.register(models.Message)
#admin.site.register(Message)
class ChatsAdmin(admin.ModelAdmin):
    """ Custom Message """

    list_display = ("message", "sender", "receiver", "timestamp")
