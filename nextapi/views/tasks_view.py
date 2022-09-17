"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from nextapi.views.taskboard_tasks_view import CreateTaskSerializer
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

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized event instance
        """
        author = request.auth.user
        serializer = CreateTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT request for a task

        Returns:
            Response -- Empty body with 204 status code
        """
        task = Task.objects.get(pk=pk)
        serializer = CreateTaskSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Delete Board"""
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TaskSerializer(serializers.ModelSerializer):
    """JSON serializer for tasks
    """
    class Meta:
        model = Task
        fields = ("id", "author_id", "task", "dateCreated",
                  "isCompleted", "timeStamp")


class CreateTaskSerializer(serializers.ModelSerializer):
    """JSON serializer for tasks
    """
    class Meta:
        model = Task
        fields = ("id", "author_id", "task", "dateCreated",
                  "isCompleted", "timeStamp")
