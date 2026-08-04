from django.db import models
from django.conf import settings

from content.models import Content

class Post(Content):
    """
    Post that can be in forums
    """

    forum = models.ForeignKey(
        "forums.Forum",
        on_delete=models.CASCADE,
        related_name="posts",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    title = models.CharField(max_length=200)
    body = models.TextField()

    tags = models.ManyToManyField(
        "forums.Tag",
        blank=True,
        related_name="posts"
    )

    def __str__(self):
        return self.title
