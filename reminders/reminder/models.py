from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    due_date = models.DateField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reminders"
    )

    def get_title(self):
        return f"Name of the reminder is: {self.title}"

    def __str__(self):
        return self.title
