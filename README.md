# Django Tasks App

A barebones Django application using Poetry for environment management and SQLite for a database.

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   poetry install
   ```
3. Activate the Poetry shell:
   ```
   poetry shell
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser (if not already done):
   ```
   python manage.py createsuperuser
   ```

## Running the application

Start the development server:

```
poetry run python manage.py runserver
```

## API Endpoints

- `GET /api/tasks/` - List all tasks
- `GET /admin/` - Django admin interface

## Structure

- `core/` - Main project settings and URL configuration
- `api/` - The API app with Task model and views
