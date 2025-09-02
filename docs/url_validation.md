# Django URL Parameter Converters

Django provides several built-in URL parameter converters for different validation needs:

## Built-in Converters

| Converter | Pattern | Description | Example |
|-----------|---------|-------------|---------|
| `str` | `<str:value>` | Any non-empty string (default) | `/posts/hello-world/` |
| `int` | `<int:value>` | Integer | `/posts/123/` |
| `slug` | `<slug:value>` | ASCII letters, numbers, hyphens, underscores | `/posts/my-post-title/` |
| `uuid` | `<uuid:value>` | UUID format | `/posts/12345678-1234-5678-9012-123456789012/` |
| `path` | `<path:value>` | String including forward slashes | `/files/path/to/file.txt/` |

## Current URL Patterns Analysis

Your current patterns:
```python
path('<int:pk>/update/', ...),    # Only accepts integers
path('<int:pk>/delete/', ...),    # Only accepts integers
path('<int:pk>/toggle/', ...),    # Only accepts integers
```

## Alternative Approaches

### 1. Using `str` converter (more flexible)
```python
# Accepts any string, then validate in view
path('<str:pk>/update/', views.TodoUpdateView.as_view(), name='todo_update'),
path('<str:pk>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
path('<str:pk>/toggle/', views.toggle_todo, name='todo_toggle'),
```

### 2. Using default (no converter specified)
```python
# Same as <str:pk>
path('<pk>/update/', views.TodoUpdateView.as_view(), name='todo_update'),
```

### 3. Custom validation in views
```python
# Keep <int:pk> but handle conversion errors gracefully
def toggle_todo(request, pk):
    try:
        pk = int(pk)  # Convert string to int
        todo = get_object_or_404(Todo, pk=pk)
        # ... rest of logic
    except ValueError:
        # Handle invalid integer conversion
        return JsonResponse({'error': 'Invalid ID format'}, status=400)
```

## When to Use Each Converter

### Use `<int:pk>` when:
- ✅ Primary keys are always integers (Django default)
- ✅ You want automatic 404 for invalid formats
- ✅ Database queries will always be integers
- ✅ API consumers expect integer IDs

### Use `<str:pk>` when:
- 🔸 Primary keys might be strings/UUIDs
- 🔸 You want to handle validation manually
- 🔸 Different ID formats in same app
- 🔸 More flexible API design

### Use `<slug:pk>` when:
- 🔸 Human-readable URLs
- 🔸 SEO-friendly identifiers
- 🔸 Primary keys based on titles/names

## For Your Todo App

**Recommendation: Keep `<int:pk>`**

Your current setup is actually ideal because:

1. **Django Model Primary Keys**: Default to integers
2. **Database Optimization**: Integer PKs are faster
3. **API Consistency**: Most APIs use integer IDs
4. **Automatic Validation**: Django handles invalid formats
5. **Clear Error Handling**: 404 for non-existent items

## Alternative: Flexible ID System

If you want more flexibility, you could support multiple ID types:

```python
# In urls.py
path('<str:identifier>/update/', views.TodoUpdateView.as_view(), name='todo_update'),

# In views.py
def get_object_or_404_flexible(model, identifier):
    """Get object by ID or other unique field"""
    try:
        # Try integer ID first
        pk = int(identifier)
        return get_object_or_404(model, pk=pk)
    except ValueError:
        # Try other fields (title, slug, etc.)
        return get_object_or_404(model, title=identifier)

class TodoUpdateView(UpdateView):
    def get_object(self):
        return get_object_or_404_flexible(Todo, self.kwargs['identifier'])
```

## API Design Considerations

### RESTful API Best Practices:
- Use integers for resource IDs
- Return 404 for non-existent resources
- Use 400 for invalid ID formats
- Keep URLs simple and predictable

### Your Current Setup Follows Best Practices:
```python
GET    /api/todos/           # List all
GET    /api/todos/123/       # Get specific (404 if not found)
PUT    /api/todos/123/       # Update specific (404 if not found)
DELETE /api/todos/123/       # Delete specific (404 if not found)
```

## Summary

**For your todo app, `<int:pk>` is perfectly fine and recommended because:**

- ✅ Follows Django conventions
- ✅ Automatic validation and error handling
- ✅ Database optimization
- ✅ REST API best practices
- ✅ Simple and predictable URLs

**When you might want different converters:**
- Multi-format IDs (int + UUID + slug)
- Human-readable URLs
- Legacy system integration
- Very large datasets (UUID for distribution)

Your current URL patterns are well-designed for a standard Django application!</content>
<parameter name="filePath">/workspaces/codespaces-blank/docs/url_validation.md
