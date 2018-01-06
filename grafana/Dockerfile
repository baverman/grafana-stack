FROM alpine:3.7 as deps

ARG GRAFANA_VERSION=4.6.3
ARG GRAFANA_CHECKSUM=75959d1cd8f66d362b3bb885481dce77693417f51c2e81ab091e3d16650f1a69

RUN apk update \
 && apk add build-base git yarn nodejs-dev go

# Build grafana binaries
RUN mkdir -p ~/go/src/github.com/grafana \
 && cd ~/go/src/github.com/grafana \
 && wget -q https://github.com/grafana/grafana/archive/v$GRAFANA_VERSION.tar.gz -O grafana.tar.gz \
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
 && cp -a conf bin public /grafana


FROM alpine:3.7
COPY --from=deps /grafana /grafana
COPY defaults.ini /grafana/conf/
WORKDIR /grafana
ENTRYPOINT ["/grafana/bin/grafana-server"]
