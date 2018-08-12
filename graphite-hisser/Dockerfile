# Base image with os requirements
# ===============================
FROM alpine:3.7 as base

ENV LANG=C.UTF-8
RUN apk update \
 && apk add python3 libffi cairo libressl ca-certificates pcre wget sqlite


# Build tools, dependencies and python packages
# =============================================
FROM base as deps

ARG GRAPHITE_VERSION
ARG HISSER_VERSION
ENV GRAPHITE_NO_PREFIX=True \
    PYTHONPATH=/pypkg/lib/python3.6/site-packages

RUN apk add python3-dev libffi-dev libressl-dev pcre-dev build-base linux-headers
RUN pip3 install --prefix=/pypkg uwsgi==2.0.17 graphite-web==$GRAPHITE_VERSION hisser==$HISSER_VERSION
#  && touch /pypkg/lib/python2.7/site-packages/zope/__init__.py


# Final image
# ===========
FROM base

ENV PATH=/pypkg/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    PYTHONPATH=/conf:/pypkg/lib/python3.6/site-packages \
    GRAPHITE_ROOT=/data \
    GRAPHITE_STORAGE_DIR=/data \
    DJANGO_SETTINGS_MODULE=graphite_local_settings \
    GRAPHITE_PORT=8080 \
    HISSER_DATA_DIR=/data

EXPOSE 2003 8080

COPY root /
COPY --from=deps /pypkg /pypkg

CMD /run.sh
