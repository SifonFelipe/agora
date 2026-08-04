from django.db import models
from django.conf import settings

from content.models import Content

class Discussion(Content):
    """
    A discussion is a place where a topic is proposed
    and is discussed below.
    """

    forum = models.ForeignKey(
        "forums.Forum",
        on_delete=models.CASCADE,
        related_name="discussions",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="discussions"
    )

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children"
    )

    title = models.CharField(max_length=300)
    context = models.TextField()

    tags = models.ManyToManyField(
        "forums.Tag",
        blank=True,
        related_name="discussions"
    )

    def __str__(self):
        return self.title
