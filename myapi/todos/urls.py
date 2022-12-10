from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .api import TodoViewSet, DeleteAllTodo, GetAllTodo, GetOneTodo

router = routers.DefaultRouter()

router.register('/todos', TodoViewSet, 'todos')

urlpatterns = [
    path('/todos/delete_all', DeleteAllTodo.as_view(), name= 'del_todo_all'),
    path('/todos/get_all', GetAllTodo.as_view(), name= 'get_todo_all'),
    path('/todos/get/<id>', GetOneTodo.as_view(), name= 'get_todo_all'),
    path('/token/', TokenObtainPairView.as_view(), name = 'token_obtain' ),
    path('/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh' ),
]

urlpatterns += router.urls