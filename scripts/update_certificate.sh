#!/bin/bash

# Запуск обновления сертификатов
docker run --rm --name certbot \
    -v "/etc/letsencrypt:/etc/letsencrypt" \
    -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
    -v "/root/cleanhouse:/var/www/html" \
    certbot/certbot renew --force-renewal

# Перезапуск Nginx через docker-compose
docker compose -f /root/cleanhouse/docker-compose.yml restart nginx
