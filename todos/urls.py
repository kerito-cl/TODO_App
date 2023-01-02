from django.urls import path
from .views import (
    TodoListView,
    TodoDetailView,
)
from . import views

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-home'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todos-detail')
]
