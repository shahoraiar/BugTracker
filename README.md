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

1. Clone the repo

```bash
git clone https://github.com/shahoraiar/BugTracker.git
cd BugTracker

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


