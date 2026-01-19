# Django Task Management API

Minimal Task Management REST API built with Django and Django REST Framework.

## Requirements
- Python 3.10+
- Django 4+

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Running the Server

Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/tasks/`.

## Running Tests

Execute unit tests:
```bash
python manage.py test
```

## API Usage

### Create a Task (POST)
**Endpoint:** `/api/tasks/`
**Body:**
```json
{
    "title": "Buy groceries",
    "status": "Pending"
}
```

### List Tasks (GET)
**Endpoint:** `/api/tasks/`

## Project Structure
- `task_app/`: Project configuration.
- `tasks/`: Task application (Models, Views, Serializers).
