from .models import Todo
from rest_framework import viewsets, permissions
from .serializer import TodoSerializer, TestTodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TestTodoSerializer