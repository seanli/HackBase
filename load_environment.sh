#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

ENV_DIR=$DIR/env

if [ ! -d "$ENV_DIR" ]; then
  virtualenv $ENV_DIR
fi

source $ENV_DIR/bin/activate
pip install -r $DIR/requirements.txt

echo "Use source $ENV_DIR/bin/activate to load virtual environment"
