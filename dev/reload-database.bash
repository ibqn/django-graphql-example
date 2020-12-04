#!/usr/bin/env bash

set -Eeuxo pipefail

DIR="$(dirname "$(readlink -f "$0")")"

printf "%s\n" "This script should be run inside the virtual environment, so that Python is available."

rm --verbose "${DIR}/../db.sqlite3" || true;
for MIG_FILE in $(find mtv_model/migrations/ -regex '^[0-9]*.*\.py' | grep --perl-regexp '[0-9]+_.*\.py')
do
    rm --verbose "${MIG_FILE}"
done

python3 "${DIR}/../manage.py" makemigrations
python3 "${DIR}/../manage.py" migrate
python3 "${DIR}/../manage.py" loaddata "${DIR}/../mtv_model/fixtures/example-data.json"
