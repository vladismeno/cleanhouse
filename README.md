# СТЕК ТЕХНОЛОГИЙ

1. **django** - фреймворк для веб-приложений на Python.
2. **sqllite** - легковесная реляционная база данных.
3. **supervisor** - программа для автоматического перезапуска упавших сервисов.
4. **screen** - утилита для работы с виртуальными консолями.
5. **docker** - платформа для контейнеризации приложений.
6. **https** - протокол безопасной передачи данных через Интернет.
7. **gunicorn** - WSGI HTTP сервер для Python веб-приложений.
8. **nginx** - веб-сервер и прокси-сервер.
9. **crontab** - программа для периодического выполнения задач в расписании.
10. **digitalocean.com** - облачная платформа для развертывания инфраструктуры.
11. **squarespace.com** - платформа для создания и управления веб-сайтами.
12. **google analytics** - сервис для сбора и анализа данных о посещении сайтов.

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

## ШПАРГАЛКА

### КОМАНДЫ ДОКЕРА

- `docker-compose down -v`: остановить и удалить Docker-контейнеры и тома.
- `docker-compose build --no-cache`: пересобрать Docker-контейнеры без кэша.
- `docker-compose up -d`: запустить Docker-контейнеры в фоновом режиме.
- `docker logs docker_name > logs.txt`: записать логи Docker в файл.
- `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' docker_name_id`: получить IP-адрес Docker-контейнера.
- `docker exec -it mysql sh`: войти в консоль MySQL Docker-контейнера.

### КОМАНДЫ MYSQL

- `mysql -u root`: войти в MySQL.
- `SHOW GRANTS FOR 'svs'@'172.26.0.4';`: показать привилегии пользователя MySQL.
- `DROP USER 'svs'@'172.26.0.4';`: удалить пользователя MySQL.

### КОМАНДЫ SUPERVISORCTL

- `supervisorctl status`: показать статус процессов.
- `supervisorctl reload`: перезагрузить конфигурацию.
- `supervisorctl update`: обновить конфигурацию.
- `supervisorctl shutdown`: выключить Supervisor.
- `supervisorctl start process_name`: запустить процесс.
- `supervisorctl stop process_name`: остановить процесс.
- `supervisorctl restart process_name`: перезапустить процесс.

### КОМАНДЫ SCREEN

- `screen -S mysession`: создать новый сеанс.
- `screen -ls`: показать доступные сеансы.
- `screen -r session_name`: переключиться на сеанс.

Подробнее о каждой команде можно узнать из соответствующих руководств и документации.
