from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Task(models.Model):
    title = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})