# Cheatsheets
## Django terminal Commands
- django-admin startproject PROJECT_NAME
- python3 manage.py runserver
- python3 manage.py startapp APP_NAME
- python3 manage.py createsuperuser

## Heroku terminal commands and configurations
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

## Create a Virtual Environment on Mac
- Check if I have virtualenv by command: which virtualenv, if not, install it in terminal by command: pip install virtualenv
- Create a virtual environment by command: virtualenv <my_env_name>
- Activate it by source <my_env_name>/bin/activate
- Deactivate: deactivate
- Check which environment you are in: which python or which pip
- Remove an environment: sudo rm -rf <my_env_name>


