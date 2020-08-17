#!/usr/bin/env bash
if ! which nginx > /dev/null 2>&1; then
    apt-get update
    apt-get -y install nginx
    service nginx start
fi
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School for the win!" | tee /data/web_static/releases/test/index.html
ln -sfn /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu /data/
chgrp -R ubuntu /data/
sed -i "45 a \ \n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
service nginx restart
