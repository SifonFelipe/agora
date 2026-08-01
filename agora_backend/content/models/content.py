from django.db import models
from django.conf import settings

class Content(models.Model):
    """
    Content envolves all possible contents (comments, posts, questions, etc)
    """
    class State(models.TextChoices):
        PUBLISHED = "published", "Published"
        IN_REVISION = "in revision", "In Revision"
        HIDDEN = "hidden", "Hidden"
        LOCKED = "locked", "Locked"
        DELETED = "deleted", "Deleted"

    forum = models.ForeignKey(
        "forums.Forum",
        on_delete=models.CASCADE,
        related_name="contents",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contents"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True, blank=True)

    state = models.CharField(
        max_length=20,
        choices=State.choices,
        default=State.PUBLISHED
    )

    tags = models.ManyToManyField(
        "forums.Tag",
        blank=True,
        related_name="contents"
    )

    def is_available(self):
        return self.State.PUBLISHED == self.state

    def __str__(self):
        return f"Content #{self.pk}"
