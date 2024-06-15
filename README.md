# СТЕК ТЕХНОЛОГИЙ

1. **django** - фреймворк для веб-приложений на Python
2. **sqllite** - легковесная реляционная база данных
3. **supervisor** - программа для автоматического перезапуска упавших сервисов
4. **screen** - утилита для работы с виртуальными консолями
5. **docker** - платформа для контейнеризации приложений
6. **https** - протокол безопасной передачи данных через Интернет
7. **gunicorn** - WSGI HTTP сервер для Python веб-приложений
8. **nginx** - веб-сервер и прокси-сервер
9. **crontab** - программа для периодического выполнения задач в расписании
10. **digitalocean.com** - облачная платформа для развертывания инфраструктуры
11. **squarespace.com** - платформа для создания и управления веб-сайтами
12. **google analytics** - сервис для сбора и анализа данных о посещении сайтов

## КАК РАЗВЕРНУТЬ ПРОЕКТ

1. Войти в хостинг через SSH: `ssh root@cleanhouse4you.com`.
2. Создать сеанс screen: `screen`.
3. Клонировать репозиторий: `git clone git@github.com:vladismeno/cleanhouse.git`.
4. Собрать статические файлы: `make collectstatic`.
5. Создать суперпользователя Django: `make createsuperuser`.
6. Применить миграции: `make migrate`.
7. Запустить Docker-контейнеры: `make up`.
8. Остановить Docker-контейнеры: `make down`.
9. Создать SSL-сертификат: `sh create_certificate.sh`.
10. Обновить SSL-сертификат: `sh update_certificate.sh`.
11. В корне проекта локально и на проде нужно создать файл с переменными DJANGO_DEBUG, SECRET_KEY

## ШПАРГАЛКА

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


### КОМАНДЫ ДЛЯ СОЗДАНИЯ И ОБНОВЛЕНИЯ СЕРТИФИКАТА SSL

## получение сертификата запускаем 1 раз
`docker run -it --rm --name certbot \
    -v "/etc/letsencrypt:/etc/letsencrypt" \
    -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
    -v "/root/cleanhouse:/var/www/html" \
    certbot/certbot certonly --webroot -w /var/www/html -d cleanhouse4you.com -d www.cleanhouse4you.com --force-renewal`


## обновление сертификата, если он устарел, в кроне каждый день в полночь
crontab -e
`0 0 * * * docker run -it --rm --name certbot \
    -v "/etc/letsencrypt:/etc/letsencrypt" \
    -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
    -v "/root/cleanhouse:/var/www/html" \
    certbot/certbot renew --quiet && \
    docker-compose -f /root/cleanhouse/docker-compose.yml restart nginx`
