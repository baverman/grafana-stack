#!/bin/sh

name=${1:-baverman/grafana-stack}
tag=${2:-1.0.2-4.4.3-1}

docker build -f Dockerfile.base -t grafana-stack.base .
docker build -f Dockerfile.deps -t grafana-stack.deps .

docker run --name extract grafana-stack.deps env GZIP=-n /bin/tar -czf - --sort=name /pypkg > req.tar.gz
docker rm -f extract

docker build -f Dockerfile -t $name:$tag -t $name:latest .
