from django.db import models
from django.conf import settings

from content.models import Content

class Comment(Content):
    """
    Comment to a Post or Discussion
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    parent = models.ForeignKey(  # Parent comment, if this is a reply to another comment
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="replies",
    )

    target = models.ForeignKey(
        "content.Post",
        on_delete=models.CASCADE,
        related_name="comments"
    )

    body = models.TextField()

    tags = models.ManyToManyField(
        "forums.Tag",
        blank=True,
        related_name="comments"
    )

