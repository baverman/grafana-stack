FROM ubuntu:17.04

COPY install-grafana.sh migrate.sh /
RUN apt-get update -y \
 && apt-get -y install --no-install-recommends \
        python2.7 libpython2.7 libffi6 openssl libpcre3 libcairo2 wget \
 && ./install-grafana.sh

# Dev dependencies
RUN apt-get -y install --no-install-recommends \
        python-dev libffi-dev libssl-dev libpcre3-dev python-pip build-essential

ENV PYTHONPATH=/conf:/pypkg/lib/python2.7/site-packages/opt/graphite/webapp:/pypkg/lib/python2.7/site-packages/opt/graphite/lib:/pypkg/lib/python2.7/site-packages
ENV PATH=/pypkg/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN mkdir -p /pypkg
RUN pip install --prefix=/pypkg setuptools wheel \
 && pip install --prefix=/pypkg uwsgi graphite-web==1.0.2 carbon==1.0.2 whisper==1.0.2 \
 && touch /pypkg/lib/python2.7/site-packages/zope/__init__.py

ENV GRAPHITE_ROOT=/data
ENV GRAPHITE_CONF_DIR=/conf
ENV GRAPHITE_STORAGE_DIR=/data/carbon

VOLUME /conf /data
EXPOSE 2003 8125 8080

CMD uwsgi --ini /conf/uwsgi.ini
