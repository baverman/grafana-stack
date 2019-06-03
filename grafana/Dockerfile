FROM alpine:3.9.4 as deps

RUN apk add --no-cache build-base git npm yarn nodejs-dev go

ARG GRAFANA_VERSION
ARG GRAFANA_CHECKSUM

# Build grafana binaries
RUN mkdir -p ~/go/src/github.com/grafana \
 && cd ~/go/src/github.com/grafana \
 && wget -q https://github.com/grafana/grafana/archive/v$GRAFANA_VERSION.tar.gz -O grafana.tar.gz \
 && sha256sum grafana.tar.gz \
 && echo "$GRAFANA_CHECKSUM  grafana.tar.gz" | sha256sum -c \
 && tar xf grafana.tar.gz \
 && mv grafana-$GRAFANA_VERSION grafana \
 && cd grafana \
 && GOPATH=~/go go run build.go setup \
 && GOPATH=~/go go run build.go build

# Build grafana static
RUN cd ~/go/src/github.com/grafana/grafana \
 && yarn install --pure-lockfile \
 && npm run build

# Prepare artifact
RUN mkdir /grafana \
 && cd ~/go/src/github.com/grafana/grafana \
 && cp -a conf bin public /grafana \
 && mv /grafana/bin/linux-amd64/* /grafana/bin/


FROM alpine:3.9.4
RUN apk add --no-cache ca-certificates
COPY --from=deps /grafana /grafana
COPY grafana.ini /grafana/conf
WORKDIR /grafana
ENTRYPOINT ["/grafana/bin/grafana-server", "--config", "/grafana/conf/grafana.ini"]
