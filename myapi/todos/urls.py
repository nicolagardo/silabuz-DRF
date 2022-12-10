from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework import routers

from .api import (
    TodoViewSet,
    DeleteAllTodo,
    GetAllTodo,
    GetOneTodo,
    UpadateTodo
)

router = routers.DefaultRouter()

router.register('/todos', TodoViewSet, 'todos')


urlpatterns = [
    path('/todos/delete_all/', DeleteAllTodo.as_view(), name= 'delete_todo_all'),
    path('/todos/get_all/', GetAllTodo.as_view(), name= 'get_todo_all'),
    path('/todos/get/<id>', GetOneTodo.as_view(), name= 'get_todo'),
    path('/todos/update/<id>', UpadateTodo.as_view(), name= 'upadtae_todo'),
    path('/token', TokenObtainPairView.as_view(), name= 'token'),
    path('/token/refresh/', TokenRefreshView.as_view(), name= 'refresh_token'),
]

urlpatterns += router.urls