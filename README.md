# Django-Admin
For Running this project we need to install
1. Django (python framework)
2. Xampp (for Database)
4. mysqlclient package (for database connection)
Now, Install any Editor platform (I choose VSCode)
after this in xampp run both Apache server and mysql server then open mysql database and create new database(name should same as in Django's setting.py page like "django_auth")
then run 
1. python manage.py makemigrations
2. python manage.py migrate
after all this for running the project
1. python manage.py runserver
on running this code
A IP address will shown "http://127.0.0.1:8000/"
