from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)
    userId      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.description
