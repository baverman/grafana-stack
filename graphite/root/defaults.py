# Secret key will be generated every time on app start if not set
SECRET_KEY = None

GRAPHITE_PORT = 8080
CARBON_PORT = 2003

# One can provide multiple retention rules via CARBON_STORAGE_SCHEMA_*
# options, see carbon docs. Rules are applied in name sort order.
# Value consist of 'pattern|retentions'
CARBON_STORAGE_SCHEMA_CARBON = r'^carbon\.|60s:1d,5m:7d,10m:30d'
CARBON_STORAGE_SCHEMA_ZDEFAULT = r'.*|60s:7d,5m:30d,30m:90d,1h:1y'

# Storage aggregations, value consist of 'pattern|xFilesFactor|aggregationMethod'
CARBON_STORAGE_AGG_MIN = r'\.min$|0.1|min'
CARBON_STORAGE_AGG_MAX = r'\.max$|0.1|max'
CARBON_STORAGE_AGG_SUM = r'\.count$|0|sum'
CARBON_STORAGE_AGG_ZDEFAULT = r'.*|0.2|average'
