#!/bin/sh

python manage.py collectstatic --noinput --clear
python manage.py migrate
gunicorn reflekt_io.wsgi --bind=0.0.0.0:80
