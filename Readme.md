# Cheatsheets
## Django terminal Commands
- ```django-admin startproject PROJECT_NAME```
- ```python3 manage.py runserver```
- ```python3 manage.py startapp APP_NAME```
- ```python3 manage.py createsuperuser```

## Django Project Deployment Configurations
- For static files, in setting.py, in MIDDLEWARE , add ```'whitenoise.middleware.WhiteNoiseMiddleware'``` after ```'django.middleware.security.SecurityMiddleware'.```, and install whitenoise.
- For security reasons:
  1. Turn DEBUG to False;
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
- ```heroku config:set DISABLE_COLLECTSTATIC=1```
- ```git push heroku master```

If the error exists and console tells you to disable collectstatic, run the following:
- ```heroku config:set DISABLE_COLLECTSTATIC=1```
- ```git push heroku master```
- ```heroku run python manage.py migrate```
- ```heroku run 'bower install --config.interactive=false;grunt prep;python manage.py collectstatic --noinput'```
- ```heroku config:unset DISABLE_COLLECTSTATIC```

## Create a Virtual Environment on Mac
- Check if I have virtualenv by command: ```which virtualenv```, if not, install it in terminal by ```pip install virtualenv```
- Create a virtual environment by ```virtualenv <my_env_name>```
- Activate it by ```source <my_env_name>/bin/activate```
- Deactivate: ```deactivate```
- Check which environment you are in: ```which python``` or ```which pip```
- Remove an environment: ```sudo rm -rf <my_env_name>```
- Delete packages in Mac terminal:```pip3 freeze | xargs pip3 uninstall -y```

## Html and Css
- Style an id using #id; style a class using .class; style an element using nothing.
- Ways to deal with different screen sizes (responsive):
  1. Add ```<meta name="viewport" content="width=device-width, initial-scale=1.0">```in head to tell the mobile devices to use a viewport that is the same width as that of the device you're using rather than a much larger one.
  2. Through media queries.
  3. Through flexbox.
  4. Through grid.
  5. Including bootstrap in our html head by adding: ```<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">```

## CS50 Web Programming

[Web page](https://cs50.harvard.edu/web/2020/)

[Youtube lectures](https://www.youtube.com/watch?v=Nn7EX3zkGUo&list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu)

