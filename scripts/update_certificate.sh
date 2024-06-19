#!/bin/bash

# Запуск обновления сертификатов
docker run --rm --name certbot \
    -v "/etc/letsencrypt:/etc/letsencrypt" \
    -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
    -v "/root/cleanhouse:/var/www/html" \
    certbot/certbot renew --quiet --config /etc/letsencrypt/renewal/www.cleanhouse4you.com.conf --cert-name www.cleanhouse4you.com

# Перезапуск Nginx через docker-compose
docker-compose -f /root/cleanhouse/docker-compose.yml restart nginx
