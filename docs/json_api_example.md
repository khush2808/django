# Simple JSON API Implementation

Here's a complete implementation of JSON APIs using Django's built-in `JsonResponse`. This approach requires no additional dependencies.

## Updated Views (`todo/views.py`)

Replace the existing content with this:

```python
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Todo
from .forms import TodoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Keep original HTML views for backward compatibility
class TodoListView(ListView):
    """Original HTML view for listing todos"""
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    """Original HTML view for creating todos"""
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:todo_list')

class TodoUpdateView(UpdateView):
    """Original HTML view for updating todos"""
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:todo_list')

class TodoDeleteView(DeleteView):
    """Original HTML view for deleting todos"""
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:todo_list')

def toggle_todo(request, pk):
    """Original HTML view for toggling todo status"""
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo:todo_list')

# New JSON API views
class TodoAPIListView(View):
    """
    JSON API for listing all todos
    GET /api/todos/
    """
    def get(self, request):
        todos = Todo.objects.all().order_by('-created_at')
        todo_list = []
        for todo in todos:
            todo_list.append({
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed,
                'created_at': todo.created_at.isoformat(),
                'updated_at': todo.updated_at.isoformat(),
            })
        return JsonResponse({'todos': todo_list, 'count': len(todo_list)})

@method_decorator(csrf_exempt, name='dispatch')
class TodoAPICreateView(View):
    """
    JSON API for creating todos
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
                'message': 'Todo created successfully'
            }, status=201)
        except KeyError as e:
            return JsonResponse({
                'error': f'Missing required field: {str(e)}'
            }, status=400)
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'error': f'Server error: {str(e)}'
            }, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class TodoAPIDetailView(View):
    """
    JSON API for todo CRUD operations
    GET /api/todos/<id>/ - Get todo details
    PUT /api/todos/<id>/ - Update todo
    DELETE /api/todos/<id>/ - Delete todo
    """
    def get(self, request, pk):
        try:
            todo = get_object_or_404(Todo, pk=pk)
            return JsonResponse({
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed,
                'created_at': todo.created_at.isoformat(),
                'updated_at': todo.updated_at.isoformat(),
            })
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)

    def put(self, request, pk):
        try:
            todo = get_object_or_404(Todo, pk=pk)
            data = json.loads(request.body)

            # Update only provided fields
            if 'title' in data:
                todo.title = data['title']
            if 'description' in data:
                todo.description = data['description']
            if 'completed' in data:
                todo.completed = data['completed']

            todo.save()

            return JsonResponse({
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed,
                'created_at': todo.created_at.isoformat(),
                'updated_at': todo.updated_at.isoformat(),
                'message': 'Todo updated successfully'
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)

    def delete(self, request, pk):
        try:
            todo = get_object_or_404(Todo, pk=pk)
            todo.delete()
            return JsonResponse({'message': 'Todo deleted successfully'})
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class TodoAPIToggleView(View):
    """
    JSON API for toggling todo completion
    PATCH /api/todos/<id>/toggle/
    """
    def patch(self, request, pk):
        try:
            todo = get_object_or_404(Todo, pk=pk)
            todo.completed = not todo.completed
            todo.save()

            return JsonResponse({
                'id': todo.id,
                'completed': todo.completed,
                'updated_at': todo.updated_at.isoformat(),
                'message': f'Todo marked as {"completed" if todo.completed else "incomplete"}'
            })
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)
```

## Updated URLs (`todo/urls.py`)

```python
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # JSON API endpoints
    path('api/todos/', views.TodoAPIListView.as_view(), name='api_todo_list'),
    path('api/todos/create/', views.TodoAPICreateView.as_view(), name='api_todo_create'),
    path('api/todos/<int:pk>/', views.TodoAPIDetailView.as_view(), name='api_todo_detail'),
    path('api/todos/<int:pk>/toggle/', views.TodoAPIToggleView.as_view(), name='api_todo_toggle'),

    # Original HTML endpoints (keep for backward compatibility)
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
    path('<int:pk>/toggle/', views.toggle_todo, name='todo_toggle'),
]
```

## Testing the APIs

### 1. List all todos
```bash
curl -X GET http://127.0.0.1:8000/api/todos/
```

### 2. Create a new todo
```bash
curl -X POST http://127.0.0.1:8000/api/todos/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn Django APIs",
    "description": "Study JSON API development",
    "completed": false
  }'
```

### 3. Get a specific todo
```bash
curl -X GET http://127.0.0.1:8000/api/todos/1/
```

### 4. Update a todo
```bash
curl -X PUT http://127.0.0.1:8000/api/todos/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn Django APIs",
    "description": "Master JSON API development with Django",
    "completed": true
  }'
```

### 5. Toggle completion status
```bash
curl -X PATCH http://127.0.0.1:8000/api/todos/1/toggle/
```

### 6. Delete a todo
```bash
curl -X DELETE http://127.0.0.1:8000/api/todos/1/
```

## Response Examples

### Successful List Response
```json
{
  "todos": [
    {
      "id": 1,
      "title": "Learn Django APIs",
      "description": "Study JSON API development",
      "completed": false,
      "created_at": "2025-09-02T10:30:00Z",
      "updated_at": "2025-09-02T10:30:00Z"
    }
  ],
  "count": 1
}
```

### Successful Create Response
```json
{
  "id": 2,
  "title": "New Todo",
  "description": "Description here",
  "completed": false,
  "created_at": "2025-09-02T10:35:00Z",
  "updated_at": "2025-09-02T10:35:00Z",
  "message": "Todo created successfully"
}
```

### Error Response
```json
{
  "error": "Missing required field: 'title'"
}
```

## Key Features

- ✅ **No additional dependencies** - Uses only Django's built-in features
- ✅ **Backward compatibility** - Original HTML views still work
- ✅ **Proper HTTP status codes** - 200, 201, 400, 404, 500
- ✅ **Error handling** - JSON error responses with descriptive messages
- ✅ **Flexible updates** - PUT allows partial updates
- ✅ **CSRF exemption** - APIs don't need CSRF tokens
- ✅ **ISO date format** - Consistent datetime serialization

This implementation gives you fully functional JSON APIs while keeping your existing HTML interface intact!</content>
<parameter name="filePath">/workspaces/codespaces-blank/docs/json_api_example.md
