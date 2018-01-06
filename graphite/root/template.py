#!/usr/bin/env python
from __future__ import print_function
import sys
import os.path
import argparse

from jinja2 import Environment, StrictUndefined, contextfilter
import defaults


def random_string(value):
    if not value:
        value = os.urandom(20).encode('hex')
    return value


@contextfilter
def split_prefix(ctx, prefix, sep='|'):
    result = []
    for k, v in sorted(ctx.items()):
        if v and k.startswith(prefix):
            name = k[len(prefix):].lower()
            result.append([name] + v.split(sep))
    return result


def load_settings():
    settings = vars(defaults)
    settings.update(os.environ)
    return settings


if __name__ == '__main__':
    env = Environment(autoescape=False, undefined=StrictUndefined, trim_blocks=True,
                      lstrip_blocks=True, auto_reload=False)

    env.filters.update({'random_string': random_string,
                        'split_prefix': split_prefix})

    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', dest='out_dir')
    parser.add_argument('--force', '-f', action='store_true', help='overwrite files in out_dir')
    parser.add_argument('template', nargs='+')

    args = parser.parse_args()
    settings = load_settings()

    for fname in args.template:
        tpl = env.from_string(open(fname).read())
        out = tpl.render(settings)
        if not out.endswith(u'\n'):
            out += u'\n'

        if args.out_dir:
            out_fname = os.path.join(args.out_dir, os.path.basename(fname))
            if args.force or not os.path.exists(out_fname):
                print('Generating', out_fname)
                fobj = open(out_fname, 'wt')
            else:
                fobj = None
                print('Skipping', out_fname)
        else:
            fobj = sys.stdout

        if fobj:
            fobj.write(out)
            fobj.flush()
