# Django Tasks App

A barebones Django application using Poetry for environment management and SQLite for a database.

## Setup

- install poetry: https://python-poetry.org/docs/ and python >= 3.11: (we suggest pyenv: https://github.com/pyenv/pyenv)

### Automated Setup

You can use the provided setup script to automatically install dependencies and create a default superuser:

```
./setup.sh
```

This script will:

1. Install Poetry dependencies
2. Create the media directory for file uploads
3. Apply database migrations
4. Create a superuser with username `defaultuser` and password `defaultuser`

### Manual Setup

If you prefer to set up manually:

1. Clone the repository
2. Install dependencies:
   ```
   poetry install --no-root
   ```
3. Create media directory:
   ```
   mkdir -p media/uploads
   ```
4. Activate the Poetry shell:
   ```
   poetry shell
   ```
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

## Running the application

Start the development server:

```
poetry run python manage.py runserver 8080
```

## Features

### Task Management

- Create, view, and manage tasks via the Django admin interface

### File Upload

- Upload files with title and description
- View a list of all uploaded files
- Download uploaded files

## API Endpoints

- `GET /api/tasks/` - List all tasks
- `GET /upload/` - File upload interface
- `GET /files/` - View uploaded files
- `GET /admin/` - Django admin interface (login with defaultuser/defaultuser)

## Structure

- `core/` - Main project settings and URL configuration
- `api/` - The API app with Task model and views
