#!/bin/bash

BASEDIR=$(dirname $0)
DJANGO_DIR=.

source $BASEDIR/load_environment.sh

python $DJANGO_DIR/manage.py runserver
