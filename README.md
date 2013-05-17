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

Setting up PostgreSQL on Mac:

* Download http://postgresapp.com/
* Restart your Mac
* Follow the steps at http://postgresapp.com/documentation

Steps for Django:

* Create the database in 'psql' using: CREATE DATABASE hackbase;
* Create a role: CREATE ROLE hackbase_admin;
* Syncdb and migrate
