#!/bin/sh

docker build -f Dockerfile.base -t grafana-stack.base .
docker build -f Dockerfile.deps -t grafana-stack.deps .

docker run --name extract grafana-stack.deps /bin/tar -czf - /pypkg > req.tar.gz
docker rm -f extract

docker build -f Dockerfile -t ${1:-grafana-stack} .
