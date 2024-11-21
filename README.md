### КОМАНДЫ ДОКЕРА

- `docker-compose down -v`: остановить и удалить Docker-контейнеры и тома
- `docker-compose build --no-cache`: пересобрать Docker-контейнеры без кэша
- `docker-compose up -d`: запустить Docker-контейнеры в фоновом режиме
- `docker logs docker_name > logs.txt`: записать логи Docker в файл
- `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' docker_name_id`: получить IP-адрес Docker-контейнера.
- `docker exec -it mysql sh`: войти в консоль MySQL Docker-контейнера
- `docker ps`: посмотреть запущенные контейнеры
- `docker ps -a`: посмотреть запущенные и остановленные контейнеры
- `docker images`: посмотреть все образы и сколько места они занимают
- `docker image prune -a`: - удаления всех неиспользуемых образов Docker, включая те, которые не используются ни в одном контейнере. Опция -a указывает, что нужно удалить все образы, включая их теги, которые больше не связаны с каким-либо контейнером
- `docker system prune --all`: - удалит все неиспользуемые образы, контейнеры, тома и сети
- `docker exec -it nginx sh -c "tail -f /var/log/supervisor/nginx.log"`: - просмотр логов nginx в supervisor

### КОМАНДЫ MYSQL

- `mysql -u root`: войти в MySQL.
- `SHOW GRANTS FOR 'svs'@'172.26.0.4';`: показать привилегии пользователя MySQL
- `DROP USER 'svs'@'172.26.0.4';`: удалить пользователя MySQL
- `SELECT user, host from mysql.user;`: посмотреть всех пользователей и права
- `CREATE USER 'svs'@'localhost' IDENTIFIED BY '111';`: создаем нужного пользователя с паролем на нужный хост
- `GRANT ALL PRIVILEGES ON *.* TO 'svs'@'localhost';`: проставляем ему все права
- `FLUSH PRIVILEGES;`: применяем изменения

### КОМАНДЫ SUPERVISORCTL

- `supervisorctl status`: показать статус процессов
- `supervisorctl reload`: перезагрузить конфигурацию
- `supervisorctl update`: обновить конфигурацию
- `supervisorctl shutdown`: выключить Supervisor
- `supervisorctl start process_name`: запустить процесс
- `supervisorctl stop process_name`: остановить процесс
- `supervisorctl restart process_name`: перезапустить процесс

### КОМАНДЫ SCREEN

- `screen -S mysession`: создать новый сеанс
- `screen -ls`: показать доступные сеансы
- `screen -r session_name`: переключиться на сеанс
- `screen -dr`: используется для подключения к сеансу
- `Ctrl + A, D`: отсоединения от сеанса
- `Ctrl + A, C`: создать новое окно
- `Ctrl + A, N`: переключиться на следующее окно
- `Ctrl + A, A`: переключиться на предыдущее окно
- `Ctrl + A, P`: переключиться на предыдущее окно
- `Ctrl + A, "`: просмотреть список окон
- `Ctrl + A, K`: закрыть текущее окно
- `Ctrl + A, D`: выход из screen (оставить сеанс активным)
- `Ctrl + D`: - выход из screen (завершить сеанс)

### КОМАНДЫ КОНСОЛИ

- `df -h`: посмотреть свободное место на диске
- `htop`: посмотреть запущенные процессы
- `kill -9 pid`: убить процесс


### ККОМАНДЫ CERTBOOT

- `apt install certbot` - установка certbot
- `certbot certificates` - показать все сертификаты
- `certbot show_account` - показать все аккаунты

## получение сертификата запускаем 1 раз (нужно запускать когда сайт поднят)
sh scripts/create_certificate.sh

## обновление сертификата, если он устарел, в кроне каждый день в полночь
chmod +x /root/cleanhouse/scripts/update_certificate.sh
sudo timedatectl set-timezone America/Los_Angeles
tail -f /var/log/update_certificate.log
crontab -e
0 0 * * * /root/cleanhouse/scripts/update_certificate.sh >> /var/log/update_certificate.log 2>&1

### этот шаблон я использовал для сайта
https://themewagon.com/themes/free-bootstrap-4-html5-business-website-template-cleaning-company/

