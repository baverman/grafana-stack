#!/bin/sh
cd $(dirname $0)
name=${1:-baverman/grafana}
version=${2:-7.0.3}
hsh=${3:-c8ce7801ff3cfbb407722817b7be1967353546177981c25f97c260b1d2ceab8a}
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
