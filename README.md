# HackBase Project

This is a basic boilerplate for quick development and deployment with Django and Heroku.

## Features:

* Facebook integration middleware and utilities
* Proper Django custom user model setup
* AJAX view endpoint decorator
* Environment-sensitive settings files
* LESS setup for better front-end design
* Pylint and PEP8 code quality check
* Production settings template with Boto, Amazon S3, and Django-Compressor

## Instruction:

1. Copy the HackBase project folder
2. Change the "hackbase" folder name to "projectname"
3. Go to "manage.py" and change "hackbase.settings" to "projectname.settings"
4. Go to "code_check.sh" and change "hackbase" in line 3 to "projectname"
5. Download and install PostgreSQL
6. Create a role named "projectname_admin" with password "localhost" and all privileges
7. Create a database named "projectname" and assign "projectname_admin" to it
8. Download and install pip
9. Run command "pip install -r requirements.txt"
10. Run command "python manage.py syncdb"
11. Run command "python manage.py migrate"
12. Run command "python manage.py createsuperuser" to make an admin account on your local environment
13. Run command "python manage.py runserver" and the application can be accessed at "localhost:8000"

### Production Setup:

1. Using Heroku, change configuration variable PROJECTNAME_ENV to "PROD"
2. Add Facebook and AWS information in "settings_prod.py"
3. Create an Amazon S3 bucket called "projectname"
4. Using Heroku, change S3_BUCKET_NAME to "projectname"
5. Using Heroku, change AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to corresponding values

### Trouble Shooting:

#### Setup PostgreSQL on Mac:

1. Download http://postgresapp.com/
2. Restart your Mac
3. Follow the steps at http://postgresapp.com/documentation
4. Create the database in 'psql' using: CREATE DATABASE projectname;
5.  Create a role: CREATE ROLE projectname_admin;
