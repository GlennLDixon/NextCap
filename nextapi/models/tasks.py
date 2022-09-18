from django.db import models
from django.contrib.auth.models import User

from nextapi.models.taskboard import TaskBoard


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    taskboards = models.ManyToManyField(TaskBoard, related_name="tasks")
    task = models.CharField(max_length=50)
    dateCreated = models.DateField()
    isCompleted = models.BooleanField(default=False)
    timeStamp = models.TimeField()
