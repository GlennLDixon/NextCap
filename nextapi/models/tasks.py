from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=50)
    dateCreated = models.DateField()
    isCompleted = models.BooleanField(default=False)
    timeStamp = models.TimeField()