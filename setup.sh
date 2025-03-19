#!/bin/bash

# Exit on error
set -e

echo "=== Setting up Django Tasks App ==="

# Install dependencies
echo "Installing dependencies with Poetry..."
poetry install --no-interaction --no-root

# Create media directory for uploads
echo "Creating media directory for uploads..."
mkdir -p media/uploads

# Apply migrations
echo "Applying database migrations..."
poetry run python manage.py migrate --no-input

# Create a superuser programmatically
echo "Creating default superuser..."
poetry run python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from django.contrib.auth.models import User
if not User.objects.filter(username='defaultuser').exists():
    User.objects.create_superuser('defaultuser', 'admin@example.com', 'defaultuser')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
"

echo "=== Setup completed successfully ==="
echo "You can now run the server with: poetry run python manage.py runserver 8080" 