# Views Documentation

Views in Django handle the business logic and connect models to templates. This app uses class-based views for most operations, located in `todo/views.py`.

## Class-Based Views

### TodoListView
- **Purpose**: Display all todo items
- **Inherits from**: `ListView`
- **Model**: `Todo`
- **Template**: `todo/todo_list.html`
- **Context variable**: `todos` (instead of default `object_list`)
- **URL**: Root path `/`
- **Functionality**: Renders the main todo list page

### TodoCreateView
- **Purpose**: Create new todo items
- **Inherits from**: `CreateView`
- **Model**: `Todo`
- **Form**: `TodoForm`
- **Template**: `todo/todo_form.html`
- **Success URL**: Redirects to todo list after creation
- **URL**: `/create/`
- **Functionality**: Handles GET (show form) and POST (create todo) requests

### TodoUpdateView
- **Purpose**: Update existing todo items
- **Inherits from**: `UpdateView`
- **Model**: `Todo`
- **Form**: `TodoForm`
- **Template**: `todo/todo_form.html`
- **Success URL**: Redirects to todo list after update
- **URL**: `/<int:pk>/update/`
- **Functionality**: Handles GET (show form with existing data) and POST (update todo) requests

### TodoDeleteView
- **Purpose**: Delete todo items
- **Inherits from**: `DeleteView`
- **Model**: `Todo`
- **Template**: `todo/todo_confirm_delete.html`
- **Success URL**: Redirects to todo list after deletion
- **URL**: `/<int:pk>/delete/`
- **Functionality**: Shows confirmation page, then deletes on POST

## Function-Based View

### toggle_todo
- **Purpose**: Toggle the completion status of a todo
- **Parameters**: `request`, `pk` (primary key of todo)
- **URL**: `/<int:pk>/toggle/`
- **Functionality**:
  1. Retrieves the todo using `get_object_or_404`
  2. Toggles the `completed` field
  3. Saves the todo
  4. Redirects back to the todo list

## View Flow

1. **List View**: User visits homepage → `TodoListView` → renders todo list
2. **Create**: User clicks "Add New Todo" → `TodoCreateView` → form → creates todo → redirect to list
3. **Update**: User clicks "Edit" → `TodoUpdateView` → form with data → updates todo → redirect to list
4. **Delete**: User clicks "Delete" → `TodoDeleteView` → confirmation → deletes todo → redirect to list
5. **Toggle**: User clicks "Mark Complete/Incomplete" → `toggle_todo` → toggles status → redirect to list

## Templates Used

- `todo_list.html`: Main list view
- `todo_form.html`: Create/update form (shared)
- `todo_confirm_delete.html`: Delete confirmation

## URL Names

All views have URL names for easy reverse URL generation:
- `todo:todo_list`
- `todo:todo_create`
- `todo:todo_update`
- `todo:todo_delete`
- `todo:todo_toggle`</content>
<parameter name="filePath">/workspaces/codespaces-blank/docs/views.md
