
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializer import TodoSerializer, TestTodoSerializer
from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer


class DeleteAllTodo(APIView):
    def delete(self, request):
        Todo.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetAllTodo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many= True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class GetOneTodo(APIView):
    def get(self, request, id):
        todo = Todo.objects.filter(id=id).first()
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class UpdateTodo(APIView):
    def update(self, request, id):
        serializer = TodoSerializer(data= request.data)
        if serializer.is_valid():
            pass
        todo = Todo.objects.filter(id=id).first()
        todo = serializer.save()
        return Response(todo.data, status=status.HTTP_202_ACCEPTED)
        