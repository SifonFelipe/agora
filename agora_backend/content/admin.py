from django.contrib import admin
from content import models as cm

@admin.register(cm.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "body")
    search_fields = ("title", "body")


@admin.register(cm.Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ("title", "context")
    search_fields = ("title", "context")


@admin.register(cm.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("discussion", "title", "body")
    search_fields = ("title", "body")


@admin.register(cm.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "body")
    search_fields = ("body",)


@admin.register(cm.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("parent", "body")
    search_fields = ("body",)
