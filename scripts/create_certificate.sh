#!/bin/bash

# нужно запускать когда сайт поднят www.cleanhouse4you.com cleanhouse4you.com и работать хотя бы по http протоколу
# так что сначала нужно скопировать папку /etc/letsencrypt/ (она есть в проекте) на сервер digital ocean
# в файле nginx.conf указаны пути к сертификатам

docker run -it --rm --name certbot \
    -v "/etc/letsencrypt:/etc/letsencrypt" \
    -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
    -v "/root/cleanhouse:/var/www/html" \
    certbot/certbot certonly --webroot -w /var/www/html \
    -d cleanhouse4you.com --force-renewal -v