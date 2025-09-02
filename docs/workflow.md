# Application Workflow

This document explains how the Django Todo app works from request to response.

## Request Flow

### 1. User Makes Request
User visits a URL like `http://127.0.0.1:8000/` in their browser.

### 2. URL Routing
- Django receives the request
- `ROOT_URLCONF` points to `todoproject.urls`
- URL pattern matches `path("", include("todo.urls"))`
- Request forwarded to `todo.urls` with remaining path

### 3. App URL Resolution
- `todo.urls` has `app_name = 'todo'`
- URL pattern `path('', views.TodoListView.as_view(), name='todo_list')` matches
- `TodoListView` is called

### 4. View Processing
- `TodoListView` inherits from `ListView`
- Queries database: `Todo.objects.all()` (ordered by `-created_at`)
- Prepares context with `todos` variable
- Renders template `todo/todo_list.html`

### 5. Template Rendering
- Template extends `base.html`
- Loops through `todos` with `{% for todo in todos %}`
- Generates HTML with Bootstrap styling
- Includes action links using `{% url %}` tags

### 6. Response
- Complete HTML page sent to browser
- Browser renders the todo list

## CRUD Operations

### Create Todo
1. User clicks "Add New Todo" → `{% url 'todo:todo_create' %}`
2. `TodoCreateView` displays empty `TodoForm`
3. User fills form and submits
4. Form validates data
5. `Todo` object created and saved
6. Redirect to `todo_list`

### Update Todo
1. User clicks "Edit" → `{% url 'todo:todo_update' todo.pk %}`
2. `TodoUpdateView` loads existing `Todo` and populates form
3. User modifies data and submits
4. Form validates and updates object
5. Redirect to `todo_list`

### Delete Todo
1. User clicks "Delete" → `{% url 'todo:todo_delete' todo.pk %}`
2. `TodoDeleteView` shows confirmation page
3. User confirms deletion
4. `Todo` object deleted from database
5. Redirect to `todo_list`

### Toggle Status
1. User clicks "Mark Complete/Incomplete" → `{% url 'todo:todo_toggle' todo.pk %}`
2. `toggle_todo` function retrieves todo
3. Toggles `completed` field
4. Saves and redirects to `todo_list`

## Database Operations

### Model-View Interaction
- Views query models using Django ORM
- `ListView` uses `get_queryset()` method
- `CreateView`/`UpdateView` use `form_valid()` for saving
- `DeleteView` handles deletion automatically

### Data Flow
```
User Input → Form Validation → Model Save → Database → Query → Context → Template → HTML
```

## Static Files and Assets

### Bootstrap Integration
- CSS/JS loaded from CDN in `base.html`
- No custom static files in this simple app
- For production: `python manage.py collectstatic`

## Error Handling

### 404 Errors
- Invalid URLs return Django's 404 page
- `get_object_or_404` in `toggle_todo` handles missing todos

### Form Validation
- Invalid form data redisplays form with error messages
- Client-side validation via HTML5 attributes
- Server-side validation via Django forms

## Security Features

### CSRF Protection
- `{% csrf_token %}` in all forms
- `CsrfViewMiddleware` enabled

### SQL Injection Prevention
- Django ORM protects against SQL injection
- All queries use parameterized statements

### XSS Prevention
- Django templates auto-escape HTML
- User input safely rendered

## Performance Considerations

### Database Queries
- `ListView` uses `select *` efficiently
- No N+1 query problems in this simple app
- Ordering done at database level

### Caching
- No caching implemented (suitable for small app)
- Static files cached by browser/CDN

### Scalability
- SQLite suitable for development/small scale
- Can be upgraded to PostgreSQL for production
- Django's class-based views are efficient

## Development Workflow

### Running the App
1. `poetry install` - Install dependencies
2. `python manage.py migrate` - Set up database
3. `python manage.py runserver` - Start development server
4. Visit `http://127.0.0.1:8000/`

### Making Changes
1. Edit models → Create migrations → Apply migrations
2. Update views/forms as needed
3. Modify templates for UI changes
4. Test functionality

### Deployment
1. Set `DEBUG = False`
2. Configure `ALLOWED_HOSTS`
3. Set up production database
4. Collect static files
5. Configure web server (nginx/gunicorn)</content>
<parameter name="filePath">/workspaces/codespaces-blank/docs/workflow.md
