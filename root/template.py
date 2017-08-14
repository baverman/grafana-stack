#!/usr/bin/env python
import sys
import os.path
import argparse

from jinja2 import Environment, StrictUndefined
import defaults


def coerce(settings, name, cnv):
    settings[name] = cnv(settings[name])


def to_bool(value):
    if value and isinstance(value, basestring):
        return value.lower() not in ('0', 'no', 'false')
    return bool(value)


def to_list_of_ints(value):
    return map(int, filter(None, value.split(',')))


# load environment vars
settings = vars(defaults)
for k, v in settings.iteritems():
    if k in os.environ:
        settings[k] = os.environ[k]

# convert strings to some more meaningful
coerce(settings, 'STATSD_PERCENTILES', to_list_of_ints)
coerce(settings, 'STATSD_ENABLE', to_bool)

# convert string schemas to dicts
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
