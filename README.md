# СТЕК ТЕХНОЛОГИЙ

1. **django** - фреймворк для веб-приложений на Python
2. **sqllite** - легковесная реляционная база данных
3. **sqllite studio** - программа для просмотра бд
4. **supervisor** - программа для автоматического перезапуска упавших сервисов
5. **screen** - утилита для работы с виртуальными консолями
6. **docker** - платформа для контейнеризации приложений
7. **https** - протокол безопасной передачи данных через Интернет
8. **gunicorn** - WSGI HTTP сервер для Python веб-приложений
9. **nginx** - веб-сервер и прокси-сервер
10. **crontab** - программа для периодического выполнения задач в расписании
11. **digitalocean.com** - облачная платформа для развертывания инфраструктуры
12. **squarespace.com** - платформа для создания и управления веб-сайтами
13. **google analytics** - сервис для сбора и анализа данных о посещении сайтов
14. **pycharm** - IDE для python
15. **bootstrap** - фреймворк для разработки адаптивных и мобильных веб-сайтов

## КАК РАЗВЕРНУТЬ ПРОЕКТ

Django не обслуживает статические файлы автоматически. Для того чтобы статические файлы работали при локальной 
разработке с DEBUG = False, необходимо настроить статический сервер, такой как WhiteNoise, или использовать другой 
веб-сервер, например, Nginx или Apache.
Если локально не отображаются статические файлы, тогда необходимо включить DEBUG = True
Проверить занят ли порт lsof -nP -iTCP -sTCP:LISTEN | grep "443

Чтобы локально поднять проект и чтобы letsencrypt не выдавал ошибку, необходимо локально скопировать все файлы, 
которые нужны для работы https /etc/letsencrypt/live/cleanhouse4you.com/
Так же когда будем разворачивать проект на digital ocean, так же не забываем о том что нужно туда скопировать эту папку
и проставляем нужные права, как минимум chmod -R 777

Если локально админка не работает и выдает ошибку CSRF verification failed. Request aborted, 
нужно использовать протокол http вместо https

Не забываем на проде выключить отладочный режим Debug=False
DJANGO_DEBUG, SECRET_KEY и letsencrypt не должны быть в открытом доступе

Нужно добавить чтобы по https можно было логиниться в админку
`CSRF_TRUSTED_ORIGINS = [
    "https://localhost",
    "https://cleanhouse4you.com",
    "https://www.cleanhouse4you.com",
    "http://cleanhouse4you.com",
    "http://www.cleanhouse4you.com",
]`

`proxy_intercept_errors on;` # теперь 404 ошибки отлавливаются на стороне nginx и отладочный режим не работает


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
11. В корне проекта локально и на проде нужно создать файл .env с переменными DEBUG, SECRET_KEY, ALLOWED_HOSTS

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


### КОМАНДЫ ДЛЯ СОЗДАНИЯ И ОБНОВЛЕНИЯ СЕРТИФИКАТА SSL

## получение сертификата запускаем 1 раз (нужно запускать когда сайт поднят)
sh scripts/create_certificate.sh

## обновление сертификата, если он устарел, в кроне каждый день в полночь
sudo timedatectl set-timezone America/Los_Angeles
crontab -e
0 0 * * * /root/cleanhouse/scripts/renew_certificates.sh >> /var/log/renew_certificates.log 2>&1
