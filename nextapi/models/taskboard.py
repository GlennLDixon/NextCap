from django.db import models
from django.contrib.auth.models import User


class TaskBoard(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
