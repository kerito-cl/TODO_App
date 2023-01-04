from django.shortcuts import render, redirect
from django.utils import timezone, dateformat
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpRequest
from .models import Todo
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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
    ordering = ['-date_updated']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(TodoListView, self).dispatch(request, *args, **kwargs)

class TodoDetailView(DetailView):
    model = Todo

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['task', 'description','status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    fields = ['status', 'task', 'description', 'date_updated']
    mydate = datetime.now()
    formatedDate = mydate.strftime("%Y-%m-%d %H:%M:%S")


    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date_updated = self.formatedDate
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
