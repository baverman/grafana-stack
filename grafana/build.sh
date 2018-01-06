#!/bin/sh
name=${1:-baverman/grafana}
version=${2:-4.6.3}
hsh=${3:-75959d1cd8f66d362b3bb885481dce77693417f51c2e81ab091e3d16650f1a69}
tag=${4:-$version}

docker build --build-arg=GRAFANA_VERSION=$version --build-arg=GRAFANA_CHECKSUM=$hsh \
             -t $name:$tag -t $name:latest grafana
