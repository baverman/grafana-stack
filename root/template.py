#!/usr/bin/env python
import sys
import os.path
import argparse

from jinja2 import Environment, StrictUndefined


class DefaultSettings:
    SECRET_KEY = 'secret-key'

    GRAPHITE_PORT = 8080
    CARBON_PORT = 2003
    CARBON_STORAGE_SCHEMA_CARBON = r'^carbon\.|60s:1d,5m:7d,10m:30d'
    CARBON_STORAGE_SCHEMA_ZDEFAULT = r'.*|60s:7d,5m:30d,30m:90d,1h:1y'

    STATSD_NAME = 'localhost'
    STATSD_PORT = 8125
    STATSD_FLUSH_INTERVAL = "60.0"
    STATSD_PERCENTILES = [50, 95, 99]
    STATSD_ENABLE = True

    GRAFANA_ROOT_URL = "http://127.0.0.1:3000/"
    GRAFANA_ADMIN_USER = 'admin'
    GRAFANA_ADMIN_PASSWORD = 'admin'


settings = vars(DefaultSettings)
settings['storage_schemas'] = []
for k, v in sorted(settings.items()):
    prefix = 'GRAPHITE_STORAGE_SCHEMA_'
    if k.startswith(prefix):
        name = k[len(prefix):].lower()
        pattern, retentions = v.split('|')
        settings['storage_schemas'].append({
            'name': name,
            'pattern': pattern,
            'retentions': retentions,
        })


env = Environment(autoescape=False, undefined=StrictUndefined, trim_blocks=True,
                  lstrip_blocks=True, auto_reload=False)

parser = argparse.ArgumentParser()
parser.add_argument('--out-dir', dest='out_dir')
parser.add_argument('template', nargs='+')

args = parser.parse_args()

for fname in args.template:
    tpl = env.from_string(open(fname).read())
    out = tpl.render(settings)
    if not out.endswith(u'\n'):
        out += u'\n'

    if args.out_dir:
        out_fname = os.path.join(args.out_dir, os.path.basename(fname))
        print 'Generating', out_fname
        fobj = open(out_fname, 'wt')
    else:
        fobj = sys.stdout

    fobj.write(out)
    fobj.flush()
