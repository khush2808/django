# Django Todo App Documentation

## Overview

This is a simple Django-based todo list application that demonstrates best practices for Django development. It allows users to create, read, update, and delete (CRUD) todo items, mark them as complete/incomplete, and provides a responsive UI using Bootstrap.

## Project Structure

The project follows Django's standard structure:

- `manage.py`: Django's command-line utility for administrative tasks
- `todoproject/`: The main Django project directory containing settings and configuration
- `todo/`: The Django app containing the todo functionality
- `db.sqlite3`: SQLite database file
- `poetry.lock` and `pyproject.toml`: Dependency management files

## Key Components

### 1. Models
The data layer is defined in `todo/models.py` with a `Todo` model that represents todo items.

### 2. Views
The business logic is handled by class-based views in `todo/views.py`:
- `TodoListView`: Displays all todos
- `TodoCreateView`: Creates new todos
- `TodoUpdateView`: Updates existing todos
- `TodoDeleteView`: Deletes todos
- `toggle_todo`: Function-based view to toggle completion status

### 3. Forms
Forms are defined in `todo/forms.py` using Django's ModelForm for creating and editing todos.

### 4. URLs
URL routing is configured in:
- `todoproject/urls.py`: Main URL configuration
- `todo/urls.py`: App-specific URL patterns

### 5. Templates
HTML templates are located in `todo/templates/todo/`:
- `base.html`: Base template with Bootstrap styling
- `todo_list.html`: List view of todos
- `todo_form.html`: Form for creating/editing todos
- `todo_confirm_delete.html`: Delete confirmation page

### 6. Admin
Django's admin interface is available but not customized in this app.

## Dependencies

- Django 5.2.5+
- Python 3.12+
- Poetry for dependency management

## Database

Uses SQLite by default, configured in `todoproject/settings.py`.

## Static Files

Static files (CSS, JS) are served via CDN (Bootstrap) and configured for production collection.</content>
<parameter name="filePath">/workspaces/codespaces-blank/docs/overview.md
