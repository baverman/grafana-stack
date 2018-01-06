#!/bin/sh
set -e

if [ ! -f /conf/carbon.conf ]; then
    /template.py --out-dir /conf /tpl/*
fi

rm /data/carbon.pid || true
mkdir -p /data/carbon/log/webapp
DJANGO_SETTINGS_MODULE=graphite_local_settings django-admin migrate --run-syncdb

exec uwsgi --ini /conf/uwsgi.ini
