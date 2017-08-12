FROM grafana-stack.base

COPY root /
ADD req.tar.gz /

ENV PYTHONPATH=/conf:/pypkg/lib/python2.7/site-packages/opt/graphite/webapp:/pypkg/lib/python2.7/site-packages/opt/graphite/lib:/pypkg/lib/python2.7/site-packages \
    PATH=/pypkg/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    GRAPHITE_ROOT=/data \
    GRAPHITE_CONF_DIR=/conf \
    GRAPHITE_STORAGE_DIR=/data/carbon

VOLUME /conf /data
EXPOSE 2003 8125 8080

CMD /run.sh
