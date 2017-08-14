# Secret key will be generated every time on app start if not set
SECRET_KEY = None

GRAPHITE_PORT = 8080
CARBON_PORT = 2003

# One can provide multiple retention rules via CARBON_STORAGE_SCHEMA_*
# options, see carbon docs. Rules are applied in name sort order.
CARBON_STORAGE_SCHEMA_CARBON = r'^carbon\.|60s:1d,5m:7d,10m:30d'
CARBON_STORAGE_SCHEMA_ZDEFAULT = r'.*|60s:7d,5m:30d,30m:90d,1h:1y'

STATSD_ENABLE = True
STATSD_NAME = 'localhost'
STATSD_PORT = 8125

# Flush interval should be grater or equal of minimal retention period.
STATSD_FLUSH_INTERVAL = '60.0'
STATSD_PERCENTILES = '50, 95, 99'

GRAFANA_ROOT_URL = 'http://127.0.0.1:3000/'
GRAFANA_ADMIN_USER = 'admin'
GRAFANA_ADMIN_PASSWORD = 'admin'
