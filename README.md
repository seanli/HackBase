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

Setting up PostgreSQL on Mac:

* Download http://postgresapp.com/
* Restart your Mac
* Follow the steps at http://postgresapp.com/documentation

Steps for Django:

* Create the database in 'psql' using: CREATE DATABASE hackbase;
* Create a role: CREATE ROLE hackbase_admin;
* Syncdb and migrate
