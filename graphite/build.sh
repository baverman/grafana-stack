#!/bin/sh
name=${1:-baverman/graphite}
version=${2:-1.1.1}
tag=${3:-$version}

docker build --build-arg=GRAPHITE_VERSION=$version -t $name:$tag -t $name:latest graphite
