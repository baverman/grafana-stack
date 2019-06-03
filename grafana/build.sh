#!/bin/sh
cd $(dirname $0)
name=${1:-baverman/grafana}
version=${2:-6.2.1}
hsh=${3:-b3ae6ed9874a8945e5a3c66ff94ef0b7689fa497928f448a0ba0149470d8086d}
tag=${4:-$version}

docker build --build-arg=GRAFANA_VERSION=$version --build-arg=GRAFANA_CHECKSUM=$hsh \
             -t $name:$tag -t $name:latest .

if [ "$PUSH" ]; then
    docker push $name:$tag
    docker push $name:latest
fi
