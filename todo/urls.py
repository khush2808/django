from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
    path('<int:pk>/toggle/', views.toggle_todo, name='todo_toggle'),
]