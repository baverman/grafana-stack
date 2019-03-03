#!/bin/sh
cd $(dirname $0)
name=${1:-baverman/grafana}
version=${2:-5.4.3}
hsh=${3:-c4d2a4723cfd7e5943e42786548ea2ccbc08cd1be80b5f447ef7309d9bd91527}
tag=${4:-$version}

docker build --build-arg=GRAFANA_VERSION=$version --build-arg=GRAFANA_CHECKSUM=$hsh \
             -t $name:$tag -t $name:latest .

if [ "$PUSH" ]; then
    docker push $name:$tag
    docker push $name:latest
fi
