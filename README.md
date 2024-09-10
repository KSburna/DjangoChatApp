# Django Chat Application

A simple real-time chat application built with Django, Bootstrap, PostgreSQL, and deployed on Render. This application allows users to log in, start chats with other users, and exchange messages.

## Features
- User authentication (sign up, login, logout)
- User-to-user chat (no chat room concept, just direct messaging)
- Password reset and change functionality
- Responsive UI built with Bootstrap
- PostgreSQL database integration
- Deployed on Render
- Email notifications via Gmail for password reset

## Prerequisites
Before setting up this project, ensure have the following installed:
- Python 3.9 or above
- PostgreSQL
- Git
- Render account (for deployment)
- Gmail account for sending emails

## Setup Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:KSburna/DjangoChatApp.git
cd DjangoChatApp
```
## 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure PostgreSQL Database

Update `settings.py` with the PostgreSQL credentials.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'db_host',
        'PORT': 'db_port',
    }
}
```

## 5. Run Migrations

```bash
python manage.py migrate
```

## 6. Create a Superuser

```bash
python manage.py createsuperuser
```

## 7. Collect Static Files

```bash
python manage.py collectstatic
```

## 8. Run the Development Server

```bash
python manage.py runserver
```

Access the app at [http://127.0.0.1:8000](http://127.0.0.1:8000).


