from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    dateCreated = models.DateField(default=timezone.now)
    isCompleted = models.BooleanField(default=False)
    timeStamp = models.TimeField(auto_now=True)
