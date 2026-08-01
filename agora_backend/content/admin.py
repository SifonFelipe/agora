from django.contrib import admin
from content import models as cm

@admin.register(cm.Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "forum", "created_at", "updated_at")
    search_fields = ("author__username",)
    list_filter = ("created_at", "updated_at")


@admin.register(cm.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("content", "title", "body")
    search_fields = ("title", "body")


@admin.register(cm.Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ("content", "title", "context")
    search_fields = ("title", "context")


@admin.register(cm.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("content", "discussion", "title", "body")
    search_fields = ("title", "body")


@admin.register(cm.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("content", "question", "body")
    search_fields = ("body",)


@admin.register(cm.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "author", "parent", "body", "created_at", "updated_at")
    search_fields = ("body", "author__username")
    list_filter = ("created_at", "updated_at")
