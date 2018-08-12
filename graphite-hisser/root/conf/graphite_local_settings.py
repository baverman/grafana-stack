# flake8: noqa
SECRET_KEY = "{{ SECRET_KEY | random_string }}"
LOGGING_CONFIG = None

STORAGE_FINDERS = (
    'hisser.graphite.Finder',
)


import logging
logging.basicConfig(level='WARN', format='[%(asctime)s] %(name)s:%(levelname)s %(message)s')

# inject local settings and proper logging
import sys
import imp
import graphite

lsm = imp.new_module('graphite.local_settings')
sys.modules['graphite.local_settings'] = lsm
vars(lsm).update((name, value) for name, value in globals().items() if name[0].isupper())

lm = imp.new_module('graphite.logger')
sys.modules['graphite.logger'] = lm
lm.log = logging.getLogger('graphite')
cache_log = logging.getLogger('graphite.cache')
rendering_log = logging.getLogger('graphite.rendering')
lm.log.cache = lambda msg, *args, **kwargs: cache_log.info(msg,*args,**kwargs)
lm.log.rendering = lambda msg, *args, **kwargs: rendering_log.info(msg,*args,**kwargs)

from graphite.settings import *
