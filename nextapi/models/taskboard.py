from django.db import models
from django.contrib.auth.models import User
from nextapi.models.tasks import Task


class TaskBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
