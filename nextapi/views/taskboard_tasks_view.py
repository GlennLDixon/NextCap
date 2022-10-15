from django.http import HttpResponseServerError
from nextapi.models.tasks import Task
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from nextapi.models import TaskBoardTask, TaskBoard


"""
POST to 'create_shared_task'

## Payload
{

    "task": "Buy California",
    "dateCreated": "01/01/22:00:00:00",
    "author": 1,
    "boardIds": [2,3,4]
}

## Component
const [newTask, setNewTask] = useState({
    task: "",
    dateCreated: new Date(),
    author: user.id,
    boardIds: []
})

const handleInput = useCallback((e) => {
        e.preventDefault()
        setNewTask({
            ...newTask,
            [e.target.name]: e.target.value,
        })
}, [setNewTask])

const handleAddTaskClicked = () => {
    createSharedTask(newTask)
}

<>
    <input name="task" onInput={handleInput}/>
    <select multiple name="boardIds" onInput={handleInput}>
        {boards.map((board) => <option value={board.id}>{board.name}</option>}
    </select>
    <button onClick={handleAddTaskClicked}>Add Task</button>
</>

## Logic / Pseudo Code
1. Create Task
2. Save Task
3. For each board_id in board_ids, create taskBoard record
"""


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

    def create(self, request):
        """Handle  operations
        Returns:
            Response -- JSON serialized event instance
        """
        # task = Task.objects.get(pk=request.data["task_id"])
        task = Task.objects.get(pk=request.data["task"])
        taskboard = TaskBoard.objects.get(pk=request.data["taskBoard"])
        taskboardtask = TaskBoardTask.objects.create(
            task=task, taskBoard=taskboard)
        serializer = CreateTaskBoardTaskSerializer(taskboardtask)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """Delete Board"""
        multiboardtask = TaskBoardTask.objects.get(pk=pk)
        multiboardtask.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskBoardTask
        fields = ('id', 'task', 'taskBoard')


class CreateTaskBoardTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskBoardTask
        fields = ('id', 'task', 'taskBoard')
