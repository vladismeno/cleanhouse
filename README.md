Эта команда остановит контейнеры и удалит их, а также удалит все тома данных, связанные с контейнерами, из памяти.
После выполнения этих шагов проект Docker Compose будет удален из памяти и больше не будет активен на вашем хосте Docker.
У меня была ошибка, после запуска образа mysql:5.7 не стартовал сервис
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d

make up
make migrate
make createsuperuser
make collectstatic∂

Пароля изначально для пользователя root нет
mysql -u root

SELECT user, host from mysql.user;
SHOW GRANTS FOR 'svs'@'172.26.0.4';

для того чтобы залогиниться в phpmyadmin - смотрим на ошибку и создаем нужного пользователя на нужный хост 

CREATE USER 'svs'@'localhost' IDENTIFIED BY '111';
GRANT ALL PRIVILEGES ON *.* TO 'svs'@'localhost';

SELECT user, host FROM mysql.user;

DROP USER 'svs'@'172.26.0.4';
FLUSH PRIVILEGES;


узнать ip докера
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql_container_name_or_id

посмотреть логи докера
docker logs docker_name


CREATE USER 'svs'@'172.18.0.3' IDENTIFIED BY '111';
GRANT ALL PRIVILEGES ON *.* TO 'svs'@'172.18.0.3';


docker exec -it mysql sh



docker swarm init
echo -e "-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgmL9ZaHYI9ZQUrtxK\nvXAExP9ttkhbSxFnYaIn2AP9KnOhRANCAAQuK9ACcpYkMiJUGE8yZ3EhMBuhquL1\nMrw2Jg2jB0p8QeLRSJyhHCybndUTlVjiHpFgkOLsDCtDUp3t2HSln4gX\n-----END PRIVATE KEY-----" | docker secret create privkey -


docker image prune -a

docker system prune


supervisorctl status




получение сертификата запускаем 1 раз
docker run -it --rm --name certbot \
    -v "/etc/letsencrypt:/etc/letsencrypt" \
    -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
    -v "/root/cleanhouse:/var/www/html" \
    certbot/certbot certonly --webroot -w /var/www/html -d cleanhouse4you.com -d www.cleanhouse4you.com --force-renewal


crontab -e

0 0 * * * docker run -it --rm --name certbot \
    -v "/etc/letsencrypt:/etc/letsencrypt" \
    -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
    -v "/root/cleanhouse:/var/www/html" \
    certbot/certbot renew --quiet && \
    docker-compose -f /root/cleanhouse/docker-compose.yml restart nginx



nano update_cert.sh

#!/bin/bash

# Путь к исполняемому файлу certbot (может потребоваться изменить в зависимости от установки)
certbot_executable="/usr/bin/certbot"

# Команда для обновления сертификата
certbot_command="$certbot_executable certonly --webroot -w /var/www/html \
-d cleanhouse4you.com -d www.cleanhouse4you.com --force-renewal"

# Запуск команды обновления сертификата
$certbot_command


chmod +x update_cert.sh


crontab -e

0 0 * * 1 /путь_к_скрипту/update_cert.sh >/dev/null 2>&1






