from django.contrib import admin
from forums.models import Forum, Tag

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "created_at")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
