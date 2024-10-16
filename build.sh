#! /usr/bin/env bash

echo "Building Project packages..."
python3 -m pip install -r requirements.txt

echo "Migrating Database..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Collecting static files..."
python3 manage.py collectstatic --noinput