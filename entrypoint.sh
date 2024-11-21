#!/bin/sh
set -e

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

exec "$@"