from django.contrib import admin
from app.models import Meeting, Note


# Register your models here.
@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    list_display = ("id", "name", "created_at")
    search_fields = (
        "id",
        "name",
    )


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    list_display = ("id", "meeting", "content", "created_at")
    search_fields = (
        "id",
        "meeting__id",
        "content",
    )
