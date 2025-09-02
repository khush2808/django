# Models Documentation

## Todo Model

Located in `todo/models.py`, the `Todo` model represents a single todo item in the database.

### Fields

- `title`: CharField (max_length=200)
  - Required field for the todo title
  - Help text: "Title of the todo item"

- `description`: TextField (blank=True)
  - Optional field for detailed description
  - Can be left empty
  - Help text: "Optional description of the todo item"

- `completed`: BooleanField (default=False)
  - Tracks whether the todo is completed
  - Defaults to False (incomplete)
  - Help text: "Whether the todo is completed"

- `created_at`: DateTimeField (auto_now_add=True)
  - Automatically set when the todo is created
  - Cannot be modified after creation
  - Help text: "Date and time when the todo was created"

- `updated_at`: DateTimeField (auto_now=True)
  - Automatically updated every time the todo is saved
  - Help text: "Date and time when the todo was last updated"

### Methods

- `__str__()`: Returns the title as the string representation of the model

### Meta Options

- `ordering = ['-created_at']`: Orders todos by creation date, newest first

### Usage

The model is used throughout the application:
- In views to query and manipulate todo data
- In forms to create/edit todos
- In templates to display todo information
- In admin interface for data management

### Database Table

The model creates a database table named `todo_todo` (appname_modelname).

### Relationships

Currently, the Todo model has no foreign key relationships. It's a standalone model representing individual todo items.</content>
<parameter name="filePath">/workspaces/codespaces-blank/docs/models.md
