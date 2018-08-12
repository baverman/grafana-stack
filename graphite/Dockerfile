# Base image with os requirements
# ===============================
FROM alpine:3.7 as base

ENV LANG=C.UTF-8
RUN apk update \
 && apk add python2 libffi cairo openssl ca-certificates pcre wget sqlite \
 && ln -sf /usr/bin/python2.7 /usr/bin/python


# Build tools, dependencies and python packages
# =============================================
FROM base as deps

ARG GRAPHITE_VERSION
ENV GRAPHITE_NO_PREFIX=True \
    PYTHONPATH=/pypkg/lib/python2.7/site-packages

RUN apk add python2-dev libffi-dev openssl-dev pcre-dev build-base linux-headers py2-pip
RUN pip2 install --prefix=/pypkg six \
 && pip2 install --prefix=/pypkg uwsgi==2.0.15 graphite-web==$GRAPHITE_VERSION fadvise==6.0.0 \
                                 carbon==$GRAPHITE_VERSION whisper==$GRAPHITE_VERSION jinja2==2.9.6 \
 && touch /pypkg/lib/python2.7/site-packages/zope/__init__.py


# Final image
# ===========
FROM base

ENV PATH=/pypkg/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    PYTHONPATH=/conf:/pypkg/lib/python2.7/site-packages \
    GRAPHITE_ROOT=/data \
    GRAPHITE_CONF_DIR=/conf \
    GRAPHITE_STORAGE_DIR=/data

EXPOSE 2003 8080
RUN mkdir /data /conf; chmod 777 /data /conf

COPY root /
COPY --from=deps /pypkg /pypkg

CMD /run.sh
