from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Task


def home(request):
    context = {
        'tasks' : Task.objects.all()
    }
    return render(request, 'tasks/home.html', context)


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'
    ordering = ['-date_posted']

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Task
    fields = ['title', 'assigned_to']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['completed']

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.assigned_to:
            return True
        return False

class TaskUpdateViewAdmin(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'assigned_to', 'completed', 'date_posted']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False