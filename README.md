- Fork this repo: https://github.com/cavela-co/cavela-llm-test
    - Some code has been provided for your convenience. You should use the ChatGPT API, but you can add any libraries or use any AI coding tools that you wish.
    - This is an app that allows the uploading of files, and the creation of tasks

**Enhance the file upload functionality such that:**

1. Implement a pdf **document classification step** that determines the type of document upon upload. 
    1. Documents will be one of:
        - Supplier quotations
        - Product specification sheets
        - Quality inspection reports
    2. We’ve prepared a small amount of sample documents here: https://drive.google.com/drive/folders/13bhnEGQVatxTxEYZo2QpIPbuCoBdhluI?usp=drive_link 
    3. When uploading a file, you should classify that file into one of the above classes:
        1. UploadedFile has a “type”: key, where key can be one of: QUOTATION, PROD_SPEC, QA_REPORT (see FileType in models.py)
2. **Generate structured information based on extracted content:**
    - If a **quotation** is uploaded, extract the following information and save it at the Quotation model:
        - Product price
        - MOQ
        - Lead time
        - Payment terms
        - Manufacturer address*
        - Shipping method
        - Shipping address
            
            **Identify missing information dynamically:**
            
            - If any of the above details are missing (e.g., MOQ is not specified in a quotation), the system should:
                - **Create actionable Tasks** (e.g., "Follow up with supplier for MOQ confirmation").
                - Store these tasks in the database in provided django Models and expose them via an API endpoint.
            - Generate:
                - use tool calling to give the estimated shipping time given the shipping address and shipping method identified above
                    - estimate_shipping_time_days(method, address) → days
                - multi-step process for choosing whether to provide a discount
                    - If there are any holiday delays in the next 90 days related to the place of manufacture, then we should add a discount that is related to the number of days of delays.
                    - Also take into account the distance from the shipping address to the manufacturer address. We want to encourage shorter round trips so that delays don’t propagate.
            - Test this feature:
                - We know that LLMs are not deterministic, but we need to know that the feature is working as expected. Implement a test and then walk us through your testing approach, including how you would handle non-deterministic LLM outputs while ensuring consistent functionality and quality.

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
