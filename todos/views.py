from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Todo


@login_required
def home(request):
    context = {
        'posts': Todo.objects.all()
    }
    return render(request, 'todos/home.html', context)
class TodoListView(ListView):
    model = Todo
    template_name = 'todos/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class TodoDetailView(DetailView):
    model = Todo
