# Grafana stack

Tiny docker images for [grafana], [graphite] and [statsdly] \([statsd] implementation\).
For example, grafana ~ 90M, graphite ~ 125M, statsdly ~ 55M.
All images are build from official sources with sane (read very opinionated :) configuration defaults.

[grafana]: https://grafana.com/
[graphite]: https://graphiteapp.org/
[statsdly]: https://github.com/baverman/statsdly
[statsd]: https://github.com/etsy/statsd


## Docker network

Grafana needs access to graphite so you should create a docker network, use
links (deprecated) or use docker-compose. All examples below assume
`grafana-stack` network.

    docker network create grafana-stack


## Graphite

Dockerhub: `baverman/graphite`.

Start container:

    mkdir -p data/carbon
    export DOCKER_USER=$(id -u):$(id -g)
    docker run -d --name graphite -p 2003:2003 --restart always --network gragana-stack \
               -v $PWD/data/carbon:/data -u $DOCKER_USER baverman/graphite

This command will start `graphite-web` and `carbon-cache` services under
current user. Only 2003 TCP port (carbon text protocol) will be exposed and all
data will be written in `data/carbon` directory.

**Ports**:

* `2003`: carbon text protocol.
* `8080`: graphite-web application, needed for grafana to fetch metrics, it's
  better to not expose it to public until you configure authorization.
* `7002`: carbon cache interface to get metrics data.

**Volumes**:

* `/data`: carbon and graphite-web storage dir.
* `/conf`: directory with all config files. Image includes
  default configs but one can override any by mounting own `/conf` volume.
  Obtaining default `/conf/carbon.conf`:

      docker run --rm baverman/graphite /template.py /tpl/carbon.conf > /tmp/carbon.conf

**Environment variables**:

* `CARBON_STORAGE_SCHEMA_*`: control retention policies in [/conf/storage-schemas.conf].
  Format is `pattern|retentions`. You can define any number of variables.
  Default retentions are:

      CARBON_STORAGE_SCHEMA_CARBON=^carbon\.|60s:1d,5m:7d,10m:30d
      CARBON_STORAGE_SCHEMA_ZDEFAULT=.*|60s:7d,5m:30d,30m:90d,1h:1y

  IMPORTANT! Default minimal retention is 60s, you MUST configure carbon clients to
  flush metrics every 60s at least. Or you will loose data.

* `CARBON_STORAGE_AGG_*`: control aggregation policies in [/conf/storage-aggregation.conf].
  Format is `pattern|xFilesFactor|aggregationMethod`. You can define any number of variables.
  Default aggregations are:

      CARBON_STORAGE_AGG_MIN=\.min$|0.1|min
      CARBON_STORAGE_AGG_MAX=\.max$|0.1|max
      CARBON_STORAGE_AGG_SUM=\.count$|0|sum
      CARBON_STORAGE_AGG_ZDEFAULT=.*|0.2|average

  Metrics ended with `.count` can be used to precisely store counters by default.

[/conf/storage-schemas.conf]: http://graphite.readthedocs.io/en/latest/config-carbon.html#storage-schemas-conf
[/conf/storage-aggregation.conf]: http://graphite.readthedocs.io/en/latest/config-carbon.html#storage-aggregation-conf
