#!/bin/sh
set -e
cd $(dirname $0)
name=${1:-baverman/grafana}
version=${2:-7.0.6}
hsh=${3:-ced0ed803072bd05243f480ebdf2acb758ceea82e6edcf95543b917b1499b771}
tag=${4:-$version}

if [ -n "$PROXY" ]; then
    proxy_opts="--build-arg=http_proxy=$PROXY --build-arg=HTTP_PROXY=$PROXY"
fi

docker build --network=host $proxy_opts \
             --build-arg=GRAFANA_VERSION=$version \
             --build-arg=GRAFANA_CHECKSUM=$hsh \
             -t $name:$tag -t $name:latest .

if [ -n "$PUSH" ]; then
    docker push $name:$tag
    docker push $name:latest
fi
