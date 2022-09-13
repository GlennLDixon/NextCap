"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nextapi.models import TaskBoard


class TaskBoardView(ViewSet):
    """Next Task views"""

    def retrieve(self, request, pk):
        """Handle GET request for single task

           Returns:
               Response -- JSON serialized task
        """

        taskboard = TaskBoard.TaskBoard.objects.get(pk=pk)
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


class TaskBoardSerializer(serializers.ModelSerializer):
    """JSON serializer for tasks
    """
    class Meta:
        model = TaskBoard
        fields = ("id", "user", "name")
