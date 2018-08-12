#!/bin/sh
set -e
django-admin migrate --run-syncdb
exec uwsgi --ini /conf/uwsgi.ini --http :$GRAPHITE_PORT
