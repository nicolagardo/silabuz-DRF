

from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Todo
from .serializer import TodoSerializer, TestTodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer


class DeleteAllTodo(APIView):
    def delete(self, request):
        Todo.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetAllTodo(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        todos = Todo.objects.all()
        seriralizer = TodoSerializer(todos, many= True)
        return Response(seriralizer.data, status=status.HTTP_200_OK)

class GetOneTodo(APIView):
    def get(self, request, id):
        todo = Todo.objects.filter(id= id).first()
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class UpadateTodo(APIView):
    def get(self, request, id):
        todo = Todo.objects.filter(id=id).first()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    def update(self, request):
        todo = Todo.objects.filter(id=id).first()
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            # todo = serializer
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)