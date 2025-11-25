# TaskForge Backend

TaskForge is a multi-tenant project management and time tracking SaaS backend
built with Django and Django REST Framework.

## Tech Stack

- Python 3.x
- Django
- Django REST Framework
- drf-spectacular (OpenAPI)
- SQLite (dev), PostgreSQL (prod-ready)

## Project Structure

- `taskforge/` – Django project + settings
- `core/` – shared base models and utilities
- `accounts/` – authentication & user-related logic (coming soon)
- `workspaces/` – multi-tenant workspaces (coming soon)
- `projects/` – projects, tasks, time tracking (coming soon)

## Getting Started (Development)

```bash
# 1. Clone repo
git clone <your-repo-url>
cd taskforge-backend

# 2. Create virtualenv
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create env file
copy .env.example .env   # or copy manually
# Edit .env and set DJANGO_SECRET_KEY

# 5. Run migrations
python manage.py migrate

# 6. Run dev server
python manage.py runserver
