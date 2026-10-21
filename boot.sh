#!/bin/sh
# Creates the table if it is missing, then serves the app.
set -e
python -c "from app import init_db; init_db()"
exec gunicorn --bind 0.0.0.0:8000 --workers 2 --access-logfile - app:app
