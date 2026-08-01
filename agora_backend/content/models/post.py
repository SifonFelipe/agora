from django.db import models

class Post(models.Model):
    """
    Post that can be in forums
    """
    content = models.OneToOneField(
        "content.Content",
        on_delete=models.CASCADE,
        related_name="post"
    )

    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
