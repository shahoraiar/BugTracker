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

2. Create and activate a virtual environment:
python -m venv .venv
# Windows
.\.venv\Scripts\activate

3. Install Python dependencies:
pip install -r requirements.txt
