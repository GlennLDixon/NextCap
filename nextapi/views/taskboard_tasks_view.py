from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from nextapi.models import TaskBoardTask


class MultiBoardTasksView(ViewSet):
    """Tasks Event View"""

    def retrieve(self, request, pk):
        """Handle Get request for a single post

        Returns:
            Response -- JSON serialized post
        """
        try:
            task = TaskBoardTask.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except TaskBoardTask.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all post

        Returns:
            Response -- JSON serialized list of post
        """
        boardtasks = TaskBoardTask.objects.all()
        task = request.query_params.get('task', None)
        taskboard = request.query_params.get('taskBoard', None)
        if task and taskboard is not None:
            boardtasks = boardtasks.filter(taskBoard_id=taskboard)
            tasks = tasks.filter(task_id=task)

        serializer = TaskSerializer(boardtasks, many=True)
        return Response(serializer.data)


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskBoardTask
        fields = ('id', 'task', 'taskBoard')
