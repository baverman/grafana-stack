#!/bin/sh
cd $(dirname $0)
name=${1:-baverman/grafana}
version=${2:-6.7.4}
hsh=${3:-8e660a03b672059f8875e4ef602d3f85250d82f7f55327cedcc95e9bbd08051c}
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
