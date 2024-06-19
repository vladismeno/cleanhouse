#!/bin/bash

# нужно запускать когда сайт поднят

docker run -it --rm --name certbot \
    -v "/etc/letsencrypt:/etc/letsencrypt" \
    -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
    -v "/root/cleanhouse:/var/www/html" \
    certbot/certbot certonly --webroot -w /var/www/html \
    -d cleanhouse4you.com -d www.cleanhouse4you.com --force-renewal -v