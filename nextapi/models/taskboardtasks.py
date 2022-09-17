from django.db import models
from nextapi.models.taskboard import TaskBoard
from nextapi.models.tasks import Task


class TaskBoardTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    taskBoard = models.ForeignKey(TaskBoard, on_delete=models.CASCADE)
