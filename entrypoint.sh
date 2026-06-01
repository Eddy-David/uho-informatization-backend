#!/bin/sh
set -e

if [ "$DATABASE" = "postgres" ]; then
  echo "Esperando a PostgreSQL..."
  while ! nc -z $DB_HOST $DB_PORT; do
    sleep 1
  done
fi

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
