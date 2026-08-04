from django.db import models
from django.conf import settings

from content.models import Content

class Question(Content):
    """
    Questions for a discussion, answering that same discussion
    """
    forum = models.ForeignKey(
        "forums.Forum",
        on_delete=models.CASCADE,
        related_name="questions",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    discussion = models.ForeignKey(
        "content.Discussion",
        on_delete=models.CASCADE,
        related_name="questions"
    )

    title = models.CharField(max_length=300)
    body = models.TextField()

    tags = models.ManyToManyField(
        "forums.Tag",
        blank=True,
        related_name="questions"
    )

    def __str__(self):
        return self.title


class Answer(models.Model):
    """
    Answers to a question

    #WARNING: check this, may be different for optimization
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    body = models.TextField()

    tags = models.ManyToManyField(
        "forums.Tag",
        blank=True,
        related_name="answers"
    )
