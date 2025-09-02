# Forms Documentation

Forms in Django handle user input validation and rendering. This app uses a ModelForm for todo operations, located in `todo/forms.py`.

## TodoForm

### Overview
- **Type**: ModelForm (inherits from `forms.ModelForm`)
- **Model**: `Todo`
- **Purpose**: Handle creation and editing of todo items

### Fields Included
The form includes these model fields:
- `title`: Required text input
- `description`: Optional textarea
- `completed`: Checkbox for completion status

### Widgets
Custom widgets are defined for better UX:
- `description`: Textarea with 3 rows for multi-line input

### Usage
The `TodoForm` is used by:
- `TodoCreateView`: For creating new todos
- `TodoUpdateView`: For editing existing todos

### Form Rendering
In templates, the form is rendered using Django's form rendering system:
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
```

### Validation
- Automatic validation based on model field constraints
- `title` is required (CharField with no blank=True)
- `description` is optional (TextField with blank=True)
- `completed` is a boolean with default False

### Form Flow
1. **GET request**: Form is displayed empty (create) or populated (update)
2. **POST request**: Form data is validated
3. **Valid**: Todo is saved, user redirected to list
4. **Invalid**: Form is re-displayed with error messages

### Template
The form uses `todo_form.html` template for both create and update operations.</content>
<parameter name="filePath">/workspaces/codespaces-blank/docs/forms.md
