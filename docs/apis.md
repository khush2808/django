# Converting to JSON APIs

There are two main approaches to create JSON APIs in Django:

## Approach 1: Simple JSON APIs (Built-in Django)

Using Django's `JsonResponse` for simple APIs without additional dependencies.

### Updated Views (`todo/views.py`)

```python
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Todo

class TodoListView(View):
    """
    API endpoint for listing all todo items.
    GET /api/todos/
    """
    def get(self, request):
        todos = Todo.objects.all().order_by('-created_at')
        todo_data = []
        for todo in todos:
            todo_data.append({
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed,
                'created_at': todo.created_at.isoformat(),
                'updated_at': todo.updated_at.isoformat(),
            })
        return JsonResponse({'todos': todo_data})

@method_decorator(csrf_exempt, name='dispatch')
class TodoCreateView(View):
    """
    API endpoint for creating a new todo item.
    POST /api/todos/
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
            todo = Todo.objects.create(
                title=data['title'],
                description=data.get('description', ''),
                completed=data.get('completed', False)
            )
            return JsonResponse({
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed,
                'created_at': todo.created_at.isoformat(),
                'updated_at': todo.updated_at.isoformat(),
            }, status=201)
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class TodoDetailView(View):
    """
    API endpoint for retrieving, updating, and deleting a specific todo.
    GET /api/todos/<id>/
    PUT /api/todos/<id>/
    DELETE /api/todos/<id>/
    """
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        return JsonResponse({
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'completed': todo.completed,
            'created_at': todo.created_at.isoformat(),
            'updated_at': todo.updated_at.isoformat(),
        })

    def put(self, request, pk):
        try:
            todo = get_object_or_404(Todo, pk=pk)
            data = json.loads(request.body)

            todo.title = data.get('title', todo.title)
            todo.description = data.get('description', todo.description)
            todo.completed = data.get('completed', todo.completed)
            todo.save()

            return JsonResponse({
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed,
                'created_at': todo.created_at.isoformat(),
                'updated_at': todo.updated_at.isoformat(),
            })
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data'}, status=400)

    def delete(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return JsonResponse({'message': 'Todo deleted successfully'})

@method_decorator(csrf_exempt, name='dispatch')
class TodoToggleView(View):
    """
    API endpoint for toggling todo completion status.
    PATCH /api/todos/<id>/toggle/
    """
    def patch(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.completed = not todo.completed
        todo.save()

        return JsonResponse({
            'id': todo.id,
            'completed': todo.completed,
            'updated_at': todo.updated_at.isoformat(),
        })
```

### Updated URLs (`todo/urls.py`)

```python
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # API endpoints
    path('api/todos/', views.TodoListView.as_view(), name='api_todo_list'),
    path('api/todos/create/', views.TodoCreateView.as_view(), name='api_todo_create'),
    path('api/todos/<int:pk>/', views.TodoDetailView.as_view(), name='api_todo_detail'),
    path('api/todos/<int:pk>/toggle/', views.TodoToggleView.as_view(), name='api_todo_toggle'),

    # Keep original HTML endpoints
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
    path('<int:pk>/toggle/', views.toggle_todo, name='todo_toggle'),
]
```

## Approach 2: Django REST Framework (Recommended)

For production APIs, Django REST Framework provides better structure, serialization, and features.

### Installation

Add to `pyproject.toml`:
```toml
dependencies = [
    "django (>=5.2.5,<6.0.0)",
    "djangorestframework (>=3.15.0,<4.0.0)"
]
```

Add to `settings.py`:
```python
INSTALLED_APPS = [
    # ... existing apps ...
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}
```

### Serializers (`todo/serializers.py`)

```python
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
```

### API Views (`todo/views.py`)

```python
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating todos.
    GET /api/todos/
    POST /api/todos/
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific todo.
    GET /api/todos/<id>/
    PUT /api/todos/<id>/
    PATCH /api/todos/<id>/
    DELETE /api/todos/<id>/
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

@api_view(['PATCH'])
def toggle_todo_api(request, pk):
    """
    API endpoint for toggling todo completion status.
    PATCH /api/todos/<id>/toggle/
    """
    try:
        todo = Todo.objects.get(pk=pk)
        todo.completed = not todo.completed
        todo.save()

        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
```

### API URLs (`todo/urls.py`)

```python
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # API endpoints
    path('api/todos/', views.TodoListCreateView.as_view(), name='api_todo_list'),
    path('api/todos/<int:pk>/', views.TodoDetailView.as_view(), name='api_todo_detail'),
    path('api/todos/<int:pk>/toggle/', views.toggle_todo_api, name='api_todo_toggle'),

    # ... existing HTML endpoints ...
]
```

## API Usage Examples

### List Todos
```bash
GET /api/todos/
```

### Create Todo
```bash
POST /api/todos/
Content-Type: application/json

{
    "title": "Learn Django APIs",
    "description": "Study REST API development",
    "completed": false
}
```

### Update Todo
```bash
PUT /api/todos/1/
Content-Type: application/json

{
    "title": "Learn Django APIs",
    "description": "Study REST API development with DRF",
    "completed": true
}
```

### Toggle Completion
```bash
PATCH /api/todos/1/toggle/
```

### Delete Todo
```bash
DELETE /api/todos/1/
```

## Key Differences

| Feature | JsonResponse | Django REST Framework |
|---------|-------------|----------------------|
| Dependencies | None | Additional package |
| Serialization | Manual | Automatic with Serializers |
| Error Handling | Manual | Built-in |
| Validation | Manual | Automatic |
| Documentation | Manual | Auto-generated |
| Pagination | Manual | Built-in |
| Authentication | Manual | Built-in |
| Permissions | Manual | Built-in |

## Recommendation

- **Use JsonResponse** for simple APIs or learning purposes
- **Use Django REST Framework** for production APIs with complex requirements

Both approaches can coexist with your existing HTML views, allowing you to serve both web pages and API endpoints from the same Django application.</content>
<parameter name="filePath">/workspaces/codespaces-blank/docs/apis.md
