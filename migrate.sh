#!/bin/sh
mkdir -p /data/carbon/log/webapp
DJANGO_SETTINGS_MODULE=graphite_local_settings django-admin migrate --run-syncdb
