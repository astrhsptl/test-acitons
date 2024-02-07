from django.contrib import admin

from .models import Notification 



class NotificationAdmin(admin.ModelAdmin):
    fields = (
        "id", "title", "description"
    )
    list_display = (
        "id", "title"
    )
    search_fields = (
        "id", "title", "description"
    )
    readonly_fields = (
        "id",
    )

admin.site.register(Notification, NotificationAdmin)