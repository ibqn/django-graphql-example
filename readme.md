# Usage

## Python environment

    bash dev/prepare.bash
    source dev/venv/bin/activate

## Start server

    python manage.py runserver

## Dump database

    python3 manage.py dumpdata --format json --indent 2 > mtv_model/fixtures/example-data.json

## Load database

    python3 manage.py loaddata mtv_model/fixtures/example-data.json
