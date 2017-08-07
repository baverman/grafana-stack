#!/bin/sh
set -e

wget --no-verbose --no-check-certificate https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana_4.4.2_amd64.deb
echo "684acc3859de06dc3b2c4081413307513bcc0ba0fe1f6872a5bf10b407dcf098  grafana_4.4.2_amd64.deb" | sha256sum -c
dpkg -i grafana_4.4.2_amd64.deb
rm grafana_4.4.2_amd64.deb
