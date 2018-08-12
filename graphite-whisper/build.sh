#!/bin/sh
name=${1:-baverman/graphite}
version=${2:-1.1.3}
tag=${3:-$version-1}

docker build --build-arg=GRAPHITE_VERSION=$version -t $name:$tag -t $name:latest graphite-whisper
