"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from nextapi.models.tasks import Task
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from nextapi.models import TaskBoard, taskboard


class TaskBoardView(ViewSet):
    """Next Task views"""

    def retrieve(self, request, pk):
        """Handle GET request for single task

           Returns:
               Response -- JSON serialized task
        """

        taskboard = TaskBoard.objects.get(pk=pk)
        serializer = TaskBoardSerializer(taskboard)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all task

            Returns:
                Response -- JSON serialized list of task
        """
        taskboards = TaskBoard.objects.all()
        serializer = TaskBoardSerializer(taskboards, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle  operations
        Returns:
            Response -- JSON serialized event instance
        """
        user = request.auth.user
        taskboard = TaskBoard.objects.create(
            user=user,
            name=request.data["name"]
        )
        serializer = CreateTaskBoardSerializer(taskboard)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """Delete Board"""
        taskboard = TaskBoard.objects.get(pk=pk)
        taskboard.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TaskBoardSerializer(serializers.ModelSerializer):
    """JSON serializer for tasks
    """
    class Meta:
        model = TaskBoard
        fields = ("id", "user", "name")


class CreateTaskBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskBoard
        fields = ("id", "user", "name")
