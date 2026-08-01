from django.db import models
from django.conf import settings

class Report(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        REVIEWED = "reviewed", "Reviewed"
        DISMISSED = "dismissed", "Dismissed"

    class Reasons(models.TextChoices):
        SPAM = "spam", "Spam"
        INAPPROPRIATE = "inappropriate", "Inappropriate"
        FAKE = "fake", "Fake"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reports"
    )

    content = models.ForeignKey(
        "content.Content",
        on_delete=models.CASCADE,
        related_name="reports"
    )

    reason = models.CharField(
        max_length=20,
        choices=Reasons.choices,
        default=Reasons.SPAM
    )
    description = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

