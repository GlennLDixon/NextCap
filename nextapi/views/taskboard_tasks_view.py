from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from nextapi.models import TaskBoardTask


class TasksView(ViewSet):
    """Tasks Event View"""

    def retrieve(self, request, pk):
        """Handle Get request for a single post

        Returns:
            Response -- JSON serialized post
        """
        try:
            task = TaskBoardTask.objects.get(pk=pk)
            serializer = PostSerializer(task)
            return Response(serializer.data)
        except TaskBoardTask.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all post

        Returns:
            Response -- JSON serialized list of post
        """
        boardtasks = TaskBoardTask.objects.all()
        = request.query_params.get('category', None)
        if category is not None:
            tasks = tasks.filter(category_id=category)

        serializer = PostSerializer(tasks, many=True)
        return Response(serializer.data)
