# BE Thu Vien

Backend Django REST API for the library management project.

## Related Frontend

Use frontend repo:
https://github.com/Dungnong/frontend-thuvien

Frontend expects backend API at:
http://127.0.0.1:8000

## Requirements

1. Python 3.11+
2. pip

## Quick Start

1. Clone repo
   git clone https://github.com/Dungnong/BE-thuvien.git

2. Go to project folder
   cd BE-thuvien

3. Create virtual environment
   python -m venv .venv

4. Activate environment (Windows PowerShell)
   .venv\Scripts\activate

5. Upgrade pip
   python -m pip install --upgrade pip

6. Install dependencies
   pip install django djangorestframework djangorestframework-simplejwt django-cors-headers django-extensions

7. Apply migrations
   python manage.py migrate

8. Run server
   python manage.py runserver 127.0.0.1:8000

## API Base Path

1. Auth
   /api/login/
   /api/token/refresh/

2. Main services
   /api/books/
   /api/loans/
   /api/core/
   /api/library/

## Team Testing Flow (BE + FE)

1. Start this backend first
2. Start frontend repo in a second terminal
3. Open frontend at http://localhost:5173

## Common Issues

1. Django import error
   Activate virtual environment before running python manage.py commands.

2. CORS issue from frontend
   Verify CORS_ALLOWED_ORIGINS in LMM/settings.py includes frontend host.

3. Database mismatch
   Re-run migrations and make sure db.sqlite3 is present.

## Notes

1. Database engine is SQLite by default.
2. This project currently runs in DEBUG mode for development.
