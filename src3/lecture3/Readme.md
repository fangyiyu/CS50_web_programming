# Commands
- django-admin startproject PROJECT_NAME
- python3 manage.py runserver
- python3 manage.py startapp APP_NAME
- python3 manage.py createsuperuser

# Heroku 
- heroku login
- git init
- heroku create APP_NAME
- heroku git:remote -a APP-NAME
- pip install gunicorn
- gunicorn LOCATION.wsgi
- touch Procfile
- In Procfile: web: gunicorn LOCATION.wsgi
- In settings.py:
  1. Add '0.0.0.0' and NAME.herokuapp.com to ALLOWED_HOSTS 
  2. Add import os and STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
- pip freeze > requirements.txt
- git add.
- git commit -m "added procfile and requirements"
- git push heroku master
- For static files, in setting.py, in MIDDLEWARE , add 'whitenoise.middleware.WhiteNoiseMiddleware' after 'django.middleware.security.SecurityMiddleware'.
