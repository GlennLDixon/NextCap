from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    dateCreated = models.DateField()
    isCompleted = models.BooleanField(default=False)
    timeStamp = models.TimeField()
