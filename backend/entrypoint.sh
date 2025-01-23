#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB__HOST $DB__PORT_CONTAINER; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python3 manage.py flush --no-input
python3 manage.py migrate
python3 manage.py collectstatic --no-input --clear


exec "$@"

#celery -A backend worker --loglevel=info