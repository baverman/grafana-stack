SECRET_KEY = '{{ SECRET_KEY }}'
LOGGING_CONFIG = None

import logging
logging.basicConfig(level='INFO')

# inject local settings
import sys
import imp
import graphite
m = imp.new_module('graphite.local_settings')
vars(m).update((name, value) for name, value in globals().items() if name[0].isupper())
sys.modules['graphite.local_settings'] = m

from graphite.settings import *
