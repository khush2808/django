# URLs Documentation

URL configuration in Django maps URLs to views. This app uses a two-level URL structure.

## Main URL Configuration (`todoproject/urls.py`)

### Purpose
The main URL configuration file routes URLs to different apps and Django's built-in features.

### URL Patterns
```python
urlpatterns = [
    path("admin/", admin.site.urls),          # Django admin interface
    path("", include("todo.urls")),           # Include todo app URLs
]
```

### Components
- **Admin URL**: `/admin/` routes to Django's admin site
- **Todo URLs**: Root path `/` includes all todo-related URLs from `todo.urls`

## App URL Configuration (`todo/urls.py`)

### Purpose
App-specific URL patterns for the todo functionality.

### App Name
- `app_name = 'todo'`: Namespacing for URL reversal

### URL Patterns
```python
urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
    path('<int:pk>/toggle/', views.toggle_todo, name='todo_toggle'),
]
```

### URL Breakdown
1. **List**: `/` → `TodoListView` (name: `todo_list`)
2. **Create**: `/create/` → `TodoCreateView` (name: `todo_create`)
3. **Update**: `/<id>/update/` → `TodoUpdateView` (name: `todo_update`)
4. **Delete**: `/<id>/delete/` → `TodoDeleteView` (name: `todo_delete`)
5. **Toggle**: `/<id>/toggle/` → `toggle_todo` (name: `todo_toggle`)

### URL Parameters
- `<int:pk>`: Integer primary key parameter for specific todo operations

### URL Reversal
URLs are reversed in templates and views using namespaced names:
- `todo:todo_list`
- `todo:todo_create`
- etc.

### Template Usage
In templates, URLs are generated using the `{% url %}` tag:
```html
<a href="{% url 'todo:todo_create' %}">Add New Todo</a>
<a href="{% url 'todo:todo_update' todo.pk %}">Edit</a>
```

### View Usage
In views, URLs are reversed using `reverse_lazy`:
```python
success_url = reverse_lazy('todo:todo_list')
```

## URL Flow
1. User visits `/` → `todo_list` → TodoListView
2. User clicks links → URL reversed to specific paths
3. Views redirect using named URLs after operations</content>
<parameter name="filePath">/workspaces/codespaces-blank/docs/urls.md
