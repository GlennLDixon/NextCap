from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from nextapi.models import TaskBoardTask, taskboard


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

    def update(self, request, pk):
        """Handle PUT request for a multi board task

        Returns:
            Response -- Empty body with 204 status code
        """
        taskboardtask = TaskBoardTask.objects.get(pk=pk)
        serializer = CreateTaskSerializer(taskboardtask, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Delete Board"""
        multiboardtask = TaskBoardTask.objects.get(pk=pk)
        multiboardtask.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskBoardTask
        fields = ('id', 'task', 'taskBoard')


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskBoardTask
        fields = ('id', 'task', 'taskBoard')
