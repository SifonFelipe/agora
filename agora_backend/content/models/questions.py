from django.db import models

class Question(models.Model):
    """
    Questions for a discussion, answering that same discussion
    """
    content = models.OneToOneField(
        "content.Content",
        on_delete=models.CASCADE,
        related_name="question"
    )

    discussion = models.ForeignKey(
        "content.Discussion",
        on_delete=models.CASCADE,
        related_name="questions"
    )

    title = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    """
    """
    content = models.OneToOneField(
        "content.Content",
        on_delete=models.CASCADE,
        related_name="answer"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    body = models.TextField()
