# Settings Documentation

Django settings are configured in `todoproject/settings.py` and control the application's behavior.

## Core Settings

### Project Paths
- `BASE_DIR`: Project root directory using `Path(__file__).resolve().parent.parent`
- Used for relative path configurations

### Security Settings
- `SECRET_KEY`: Random key for cryptographic signing (keep secret in production)
- `DEBUG = True`: Enables debug mode (set to False in production)
- `ALLOWED_HOSTS = []`: Empty for development (add domains in production)

## Application Configuration

### INSTALLED_APPS
List of Django apps enabled:
```python
INSTALLED_APPS = [
    "django.contrib.admin",        # Admin interface
    "django.contrib.auth",         # User authentication
    "django.contrib.contenttypes", # Content type framework
    "django.contrib.sessions",     # Session management
    "django.contrib.messages",     # Message framework
    "django.contrib.staticfiles",  # Static file handling
    "todo",                        # Our custom app
]
```

### MIDDLEWARE
Request/response processing middleware:
- Security middleware
- Session middleware
- Common middleware
- CSRF protection
- Authentication middleware
- Message middleware
- Clickjacking protection

## URL and Template Configuration

### ROOT_URLCONF
- Points to `todoproject.urls` for main URL routing

### TEMPLATES
- Uses Django template backend
- `DIRS = []`: No global template directories
- `APP_DIRS = True`: Templates found in app directories
- Context processors for request, auth, and messages

## Database Configuration

### DATABASES
- Uses SQLite by default
- Database file: `BASE_DIR / "db.sqlite3"`
- Can be changed to PostgreSQL, MySQL, etc. for production

## Internationalization

- `LANGUAGE_CODE = "en-us"`
- `TIME_ZONE = "UTC"`
- `USE_I18N = True`: Enable internationalization
- `USE_TZ = True`: Use timezone-aware datetimes

## Static and Media Files

### Static Files
- `STATIC_URL = "static/"`: URL prefix for static files
- `STATIC_ROOT = BASE_DIR / "staticfiles"`: Collection directory for production

### Media Files
- `MEDIA_URL = "/media/"`: URL prefix for user-uploaded files
- `MEDIA_ROOT = BASE_DIR / "media"`: Storage directory for uploads

## Other Settings

### Password Validation
Four built-in validators:
- User attribute similarity
- Minimum length
- Common password
- Numeric password

### Default Auto Field
- `DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"`: Primary key type

## Development vs Production

### Development Settings
- `DEBUG = True`
- `ALLOWED_HOSTS = []`
- Detailed error pages
- No caching

### Production Considerations
- `DEBUG = False`
- Set `ALLOWED_HOSTS` to your domain
- Use environment variables for `SECRET_KEY`
- Configure proper database
- Set up static file serving
- Enable security middleware
- Configure logging
- Use HTTPS</content>
<parameter name="filePath">/workspaces/codespaces-blank/docs/settings.md
