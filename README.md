# Todo Django App

A simple Django-based todo list application demonstrating best practices for Django development.

## Features

- Create, read, update, and delete (CRUD) todo items
- Mark todos as complete/incomplete
- Responsive UI with Bootstrap
- Unit tests for models and views
- Professional project structure

## Prerequisites

- Python 3.9+
- Poetry (for dependency management)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-django
   ```

2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

3. Apply database migrations:
   ```bash
   poetry run python manage.py migrate
   ```

4. Run the development server:
   ```bash
   poetry run python manage.py runserver
   ```

5. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

- **View Todos**: The homepage displays all your todos
- **Add Todo**: Click "Add New Todo" to create a new item
- **Edit Todo**: Click "Edit" next to any todo to modify it
- **Delete Todo**: Click "Delete" to remove a todo (with confirmation)
- **Toggle Status**: Click "Mark Complete/Incomplete" to change the status

## Project Structure

```
todo-django/
├── todoproject/          # Main Django project
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── todo/                 # Todo app
│   ├── migrations/       # Database migrations
│   ├── templates/todo/   # HTML templates
│   ├── models.py         # Todo model
│   ├── views.py          # View classes and functions
│   ├── forms.py          # Todo form
│   ├── urls.py           # App URL configuration
│   └── tests.py          # Unit tests
├── pyproject.toml        # Poetry configuration
├── poetry.lock           # Dependency lock file
└── README.md             # This file
```

## API Endpoints

- `GET /` - List all todos
- `GET /create/` - Show create form
- `POST /create/` - Create new todo
- `GET /<id>/update/` - Show update form
- `POST /<id>/update/` - Update todo
- `GET /<id>/delete/` - Show delete confirmation
- `POST /<id>/delete/` - Delete todo
- `GET /<id>/toggle/` - Toggle todo completion status

## Testing

Run the test suite:

```bash
poetry run python manage.py test
```

## Deployment

For production deployment:

1. Set `DEBUG = False` in `todoproject/settings.py`
2. Configure `SECRET_KEY` securely
3. Set up a production database
4. Configure static files serving
5. Use a WSGI server like Gunicorn

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License.