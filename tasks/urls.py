from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskUpdateViewAdmin
)
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks-home'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/admin_update', TaskUpdateViewAdmin.as_view(), name='task-admin_update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
]