from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

class TodoListView(ListView):
    """
    View for listing all todo items.
    """
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    """
    View for creating a new todo item.
    """
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:todo_list')

class TodoUpdateView(UpdateView):
    """
    View for updating an existing todo item.
    """
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:todo_list')

class TodoDeleteView(DeleteView):
    """
    View for deleting a todo item.
    """
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:todo_list')

def toggle_todo(request, pk):
    """
    View to toggle the completed status of a todo item.
    """
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo:todo_list')
