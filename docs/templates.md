# Templates Documentation

Templates in Django render HTML with dynamic content. This app uses Django templates with Bootstrap for styling.

## Template Structure

Templates are located in `todo/templates/todo/` and follow Django's template inheritance.

## Base Template (`base.html`)

### Purpose
Provides common HTML structure and styling for all pages.

### Features
- HTML5 doctype and meta tags
- Bootstrap CSS and JS from CDN
- Navigation bar with app title
- Container div for page content
- Block system for content injection

### Block Structure
- `{% block title %}`: Page title (defaults to "Todo List")
- `{% block content %}`: Main page content

## Todo List Template (`todo_list.html`)

### Purpose
Displays all todo items in a list format.

### Features
- Extends `base.html`
- Shows "Add New Todo" button
- Lists todos with Bootstrap styling
- Shows title, description, creation date
- Action buttons: Edit, Delete, Toggle status
- Handles empty state ("No todos yet")

### Dynamic Elements
- `{% for todo in todos %}`: Loops through todo items
- `{% if todo.completed %}`: Conditional styling for completed items
- `{% url %}` tags for link generation
- Date formatting: `{{ todo.created_at|date:"M d, Y H:i" }}`

## Todo Form Template (`todo_form.html`)

### Purpose
Form for creating and editing todos (shared template).

### Features
- Extends `base.html`
- Django form rendering
- CSRF protection
- Bootstrap form styling
- Submit button

### Form Handling
- `{{ form.as_p }}`: Renders form fields as paragraphs
- `{% csrf_token %}`: Cross-site request forgery protection
- Form method: POST

## Delete Confirmation Template (`todo_confirm_delete.html`)

### Purpose
Confirms todo deletion to prevent accidental removal.

### Features
- Extends `base.html`
- Shows todo title
- Confirmation form with POST method
- Cancel link back to list

## Template Inheritance Flow

```
base.html
├── todo_list.html
├── todo_form.html (used for create and update)
└── todo_confirm_delete.html
```

## Static Files

- Bootstrap CSS/JS loaded from CDN
- No custom static files in this app
- Static file configuration in `settings.py` for production

## Context Processors

Enabled in `settings.py`:
- `django.template.context_processors.request`
- `django.contrib.auth.context_processors.auth`
- `django.contrib.messages.context_processors.messages`

## Template Tags Used

- `{% extends %}`: Template inheritance
- `{% block %}`: Content blocks
- `{% if %}`, `{% for %}`: Control flow
- `{% url %}`: URL reversal
- `{{ variable }}`: Variable output
- `{{ variable|filter }}`: Template filters (date formatting)

## Responsive Design

- Bootstrap classes for responsive layout
- Mobile-friendly navigation and forms
- Flexible grid system for different screen sizes</content>
<parameter name="filePath">/workspaces/codespaces-blank/docs/templates.md
