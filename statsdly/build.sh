#!/bin/sh
name=${1:-baverman/statsdly}
version=${2:-0.4}
tag=${3:-$version}

docker build --build-arg=STATSDLY_VERSION=$version -t $name:$tag -t $name:latest statsdly
