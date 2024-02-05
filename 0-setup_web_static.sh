#!/usr/bin/env bash
# create directories to deploy website
apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "Hello World! AirBnB" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
string="\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}"
sed -i "s/^\tserver_name .*;$/&\n$string/" /etc/nginx/sites-available/default
service nginx restart
