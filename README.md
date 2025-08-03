# BugTracker

A simple bug tracking system built with Django, Django REST Framework, Django Channels, and Redis for real-time WebSocket updates.

---

## Features

- User authentication with JWT token
- Create and manage Projects and Bugs
- Real-time bug updates using WebSocket (Django Channels + Redis)
- Bootstrap-based responsive UI for bug list per project
- REST API for Projects and Bugs

---

## Requirements

- Python 3.8+
- Redis Server (for Channels layer) 5+
- Git

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/shahoraiar/BugTracker.git
cd BugTracker
```

2. Create and activate a virtual environment:
 ```bash
python -m venv .venv
```

# Windows
```bash
.\.venv\Scripts\activate
```

3. Install Python dependencies:
pip install -r requirements.txt

4. Install and start Redis server (version 5+):
Start Redis server locally (default port 6379)

5. Apply database migrations:
python manage.py migrate

6. Create a superuser (for admin access):
python manage.py createsuperuser

7. Collect static files (optional, for production):
python manage.py collectstatic

## 8. Running the Project
Run the ASGI server with WebSocket support using daphne or uvicorn:
# Using daphne
daphne -p 8000 bugtracker.asgi:application


Admin Panel: http://127.0.0.1:8000/admin/
Bug List Page: http://127.0.0.1:8000/bug-list/<project_id>/

API Endpoints
| Endpoint              | Description                    | Method         | Auth Required |
| --------------------- | ------------------------------ | -------------- | ------------- |
| `/api/token/`         | Obtain JWT token               | POST           | No            |
| `/api/token/refresh/` | Refresh JWT token              | POST           | No            |
| `/api/projects/`      | List/Create Projects           | GET/POST       | Yes           |
| `/api/projects/<id>/` | Retrieve/Update/Delete Project | GET/PUT/DELETE | Yes           |
| `/api/bugs/`          | List/Create Bugs               | GET/POST       | Yes           |
| `/api/bugs/<id>/`     | Retrieve/Update/Delete Bug     | GET/PUT/DELETE | Yes           |


WebSocket Support
* WebSocket URL pattern: ws://<host>/ws/project/<project_id>/
* Clients connected to a project's WebSocket room receive real-time notifications when new bugs are created on that project.

Redis Version
This project requires Redis version 5 or higher to support Django Channels' channel layer features correctly. Lower versions may cause errors such as unknown command 'BZPOPMIN'.


Project Structure (key files)
bugtracker/
├── bugtracker/
│   ├── asgi.py        # ASGI application setup for Channels
│   ├── settings.py    # Django project settings
│   ├── urls.py        # URL routing including API and pages
│   └── wsgi.py
├── tracker/
│   ├── models.py      # Project and Bug models
│   ├── views.py       # bug_list_view and API views
│   ├── serializers.py # DRF serializers
│   ├── consumers.py   # WebSocket consumer for live updates
│   ├── routing.py     # WebSocket URL routing
│   └── admin.py       # Model registrations
├── requirements.txt
└── manage.py


Author
Shahoraiar Hossain
