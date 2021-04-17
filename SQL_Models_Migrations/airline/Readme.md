1. Every time we make changes in models.py we have to make migrations and then migrate:
- python3 manage.py makemigrations (create python files that will create or edit our database to be able to store what in the models)
- python3 manage.py migrate (apply the migrations to the database)

2. Run python3 manage.py shell to add information and manipulate database.
