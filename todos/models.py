from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status_choices = (('NotStarted', 'NotStarted'),
        ('OnGoing', 'OnGoing'), 
        ('Completed','Completed'),
        )
    status = models.CharField(max_length = 100, choices = status_choices,
            default="NotStarted")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todos-home')
