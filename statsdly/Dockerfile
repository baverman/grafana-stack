FROM alpine:3.7
ARG STATSDLY_VERSION=0.4

RUN apk update \
 && apk add python3 \
 && pip3 install statsdly==$STATSDLY_VERSION \
 && rm -rf /usr/lib/python3.6/site-packages/pip /usr/lib/python3.6/distutils /usr/lib/python3.6/pydoc_data \
           /usr/lib/python3.6/lib2to3 /usr/lib/python3.6/ensurepip /usr/lib/python3.6/asyncio \
           /usr/lib/python3.6/email /usr/lib/python3.6/xml /usr/lib/python3.6/site-packages/setuptools \
           /usr/lib/python3.6/multiprocessing /usr/lib/python3.6/unittest /var/cache/apk /usr/share/terminfo

ENTRYPOINT ["/usr/bin/python3", "-m", "statsdly"]
