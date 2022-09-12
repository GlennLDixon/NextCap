"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nextapi.models import Task


class TaskView(ViewSet):
    """Next Task views"""

    def retrieve(self, request, pk):
        """Handle GET request for single task

           Returns:
               Response -- JSON serialized task
        """

        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all task

            Returns:
                Response -- JSON serialized list of task
        """
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskSerializer(serializers.ModelSerializer):
    """JSON serializer for tasks
    """
    class Meta:
        model = Task
        fields = ("id", "task", "dateCreated", "isCompleted", "timeStamp")
