from django.contrib import admin

# Register your models here.
from .models import Project, Bug

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "created_at", "updated_at")
    search_fields = ("name", "description", "owner__username")
    list_filter = ("owner",)
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "project", "status", "priority", "created_by", "created_at")
    search_fields = ("title", "description", "project__name", "created_by__username")
    list_filter = ("status", "priority", "project")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)