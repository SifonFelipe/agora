from django.db import models
from django.conf import settings

class Comment(models.Model):
    """
    Comment to a Post or Discussion
    """
    content = models.OneToOneField(  # Content of the comment
        "content.Content",
        on_delete=models.CASCADE,
        related_name="comment"
    )

    parent = models.ForeignKey(  # Parent comment, if this is a reply to another comment
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="replies",
    )

    target = models.ForeignKey(
        "content.Content",
        on_delete=models.CASCADE,
        related_name="comments"
    )

    body = models.TextField()

