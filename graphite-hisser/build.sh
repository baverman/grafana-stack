#!/bin/sh
name=${1:-baverman/graphite-hisser}
graphite_version=${2:-1.1.3}
hisser_version=${3:-0.9}
tag=${4:-$graphite_version-$hisser_version-1}

docker build --build-arg=GRAPHITE_VERSION=$graphite_version \
             --build-arg=HISSER_VERSION=$hisser_version \
             -t $name:$tag -t $name:latest graphite-hisser
