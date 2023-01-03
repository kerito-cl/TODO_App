from django.urls import path
from .views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView
)
from . import views

urlpatterns = [
    path('', TodoListView.as_view(), name='todos-home'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='post-detail'),
    path('todo/new/', TodoCreateView.as_view(), name='post-create'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='post-update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='post-delete'),
]
