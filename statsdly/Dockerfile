FROM alpine:3.7
ARG STATSDLY_VERSION=0.4

RUN apk update \
 && apk add python3 \
 && pip3 install statsdly==$STATSDLY_VERSION

ENTRYPOINT ["/usr/bin/statsdly"]
