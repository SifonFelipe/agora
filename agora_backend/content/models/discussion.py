from django.db import models

class Discussion(models.Model):
    """
    A discussion is a place where a topic is proposed
    and is discussed below.
    """
    content = models.OneToOneField(
        "content.Content",
        on_delete=models.CASCADE,
        related_name="discussion",
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

    def __str__(self):
        return self.title
