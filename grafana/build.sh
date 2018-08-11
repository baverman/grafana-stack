#!/bin/sh
name=${1:-baverman/grafana}
version=${2:-5.2.2}
hsh=${3:-4267618981b93135644dd88f6f1cd2f1aa184b96ff845c8164c38dcb6e3fd777}
tag=${4:-$version}

docker build --build-arg=GRAFANA_VERSION=$version --build-arg=GRAFANA_CHECKSUM=$hsh \
             -t $name:$tag -t $name:latest grafana
