## Django terminal Commands
- ```django-admin startproject PROJECT_NAME```
- ```python3 manage.py runserver```
- ```python3 manage.py startapp APP_NAME```
- ```python3 manage.py createsuperuser```

## Django Project Deployment Configurations
- For static files, in setting.py, in MIDDLEWARE , add ```'whitenoise.middleware.WhiteNoiseMiddleware'``` after ```'django.middleware.security.SecurityMiddleware'.```, and install whitenoise.
- For security reasons:
  1. Turn DEBUG to FALSE and add ALLOWED_HOSTS;
  2. In settings.py: Add ```'0.0.0.0'``` and ```NAME.herokuapp.com``` to ALLOWED_HOSTS; 
  3. Add ```from decouple import config```, change SECRET KEY to ```SECRET_KEY = config('SECRET_KEY')```;
  4. Add .env file in the root directory; In the .env file, add ```SECRET KEY = <your secret key>```;
  5. Add .gitignore in the root directory; In the .gitignore file, add ```.env```.

## Deploy on Heroku
- ```heroku login```
- ```git init```
- ```heroku create APP_NAME```
- ```heroku git:remote -a APP-NAME```

In the Django project, do
- ```pip install gunicorn``` if gunicorn is not installed before
- ```gunicorn LOCATION.wsgi```
- ```touch Procfile```
- In Procfile: ```web: gunicorn LOCATION.wsgi```, note the space before gunicorn
- ```pip freeze > requirements.txt```
- ```git add .```
- ```git commit -m "added procfile and requirements"```
- ```git push heroku master```

## Create a Virtual Environment on Mac
- Check if I have virtualenv by command: ```which virtualenv```, if not, install it in terminal by ```pip install virtualenv```
- Create a virtual environment by ```virtualenv <my_env_name>```
- Activate it by ```source <my_env_name>/bin/activate```
- Deactivate: ```deactivate```
- Check which environment you are in: ```which python``` or ```which pip```
- Remove an environment: ```sudo rm -rf <my_env_name>```
- Delete packages in Mac terminal:```pip3 freeze | xargs pip3 uninstall -y```


