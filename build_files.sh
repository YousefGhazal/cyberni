#!/bin/bash

# Build the project
echo "Building the project..."
python3 -m pip install -r requirements.txt

echo "Make Migration..."
python3 manage.py migrate --noinput

echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear

export DJANGO_SUPERUSER_PASSWORD='1234'
python3 manage.py createsuperuser --noinput --username admin --email 'admin@gmail.com'
