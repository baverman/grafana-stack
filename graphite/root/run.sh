#!/bin/sh
set -e

/template.py --out-dir /conf /tpl/*

rm /data/carbon.pid || true
mkdir -p /data/carbon/log/webapp
DJANGO_SETTINGS_MODULE=graphite_local_settings django-admin migrate --run-syncdb

exec uwsgi --ini /conf/uwsgi.ini
