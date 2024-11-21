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
3. Если виртуалка новая, необходимо сгенерить новый ключ `ssh-keygen -t rsa -b 4096 -C "vladismeno@gmail.com"`
4. Берем ключ `cat ~/.ssh/id_rsa.pub` и добавляем его в git, там где лежит наш проект
5. Клонировать репозиторий: `git clone git@github.com:vladismeno/cleanhouse.git`.
6. sudo apt-get install make
6. Необходимо установить докер, если он не установлен. Установка докера показана ниже
6. Собрать статические файлы: `make collectstatic`.
7. Создать суперпользователя Django: `make createsuperuser`.
8. Применить миграции: `make migrate`.
9. Запустить Docker-контейнеры: `make up`.
10. Остановить Docker-контейнеры: `make down`.
11. Создать SSL-сертификат: `sh create_certificate.sh`.
12. Обновить SSL-сертификат: `sh update_certificate.sh`.
13. В корне проекта локально и на проде нужно создать файл .env с переменными DEBUG, SECRET_KEY, ALLOWED_HOSTS

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
chmod +x /root/cleanhouse/scripts/update_certificate.sh
sudo timedatectl set-timezone America/Los_Angeles
tail -f /var/log/update_certificate.log
crontab -e
0 0 * * * /root/cleanhouse/scripts/update_certificate.sh >> /var/log/update_certificate.log 2>&1


## если не запускается nginx
sudo nginx -t
sudo scp -r /etc/letsencrypt root@137.184.176.40:/etc/
sudo chmod -R 777 /etc/letsencrypt/live/www.cleanhouse4you.com/
https://themewagon.com/themes/free-bootstrap-4-html5-business-website-template-cleaning-company/



## если не получается скачать проект с git
ssh-keygen -t rsa -b 4096 -C "vladismeno@gmail.com"
less /root/.ssh/id_rsa.pub
Копируем содержимое файла в git SSH keys


Если не запускается nginx, или запускается, но правильно не работает, здесь можем посмотреть ошибки
docker exec -it nginx tail -f /var/log/supervisor/nginx.log
docker exec -it nginx tail -f /var/log/supervisor/nginx_err.log
stdout_logfile=/var/log/supervisor/nginx.log
stderr_logfile=/var/log/supervisor/nginx_err.log



### ДЕПЛОЙ ПРОЕКТА НА DIGITAL OCEAN
1. Логинимся в https://cloud.digitalocean.com/login с помощью почты 
2. Создаем дроплет за 4$ в месяц без докера, выбираем вход по паролю (почему-то когда выбираю по ssh ключу, то команда scp не работает)
3. ssh root@cleanhouse4you.com, вводим пароль, который выбрали во втором пункте, если не получается зайти на сервер, 
   возможно нужно здесь почистить запись: `vim /Users/svs/.ssh/known_hosts` а именно удалить строку с cleanhouse4you.com. 
   Ну ли просто зайти ssh root@ip_droplet
4. Создать сеанс screen: `screen`.
5. Устанавливаем докер
 - sudo apt update && sudo apt upgrade -y
 - sudo mkdir -p /etc/apt/keyrings
 - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
 - echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
 - sudo apt update
 - sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
6. Устанавливаем make: `apt-get install make`
7. Если виртуалка новая, тогда чтобы выполнить команду git clone, необходимо сгенерить новый ключ `ssh-keygen -t rsa -b 4096 -C "vladismeno@gmail.com"`
8. Берем ключ `cat ~/.ssh/id_rsa.pub` и добавляем его в git, там где лежит наш проект
9. Клонировать репозиторий: `git clone git@github.com:vladismeno/cleanhouse.git`
10. Переходим в корень проекта `cd cleanhouse`
11. Создаем файл .env `vim .env` и добвавляем следующие строки, без них не будет работать проект, в ALLOWED_HOSTS необходимо добавить ip_droplet
DEBUG=True
SECRET_KEY='django-insecure-8q^tpixw1go4@uk5a6q0s7+*b)(tltvi^b**%cffzhmm54lef#'
ALLOWED_HOSTS='localhost,127.0.0.1,0.0.0.0,192.168.1.108,137.184.176.40,cleanhouse4you.com,www.cleanhouse4you.com'
12. Выполняем команду make up
13. Чтобы отображались статические файлы, выполняем `make collectstatic`
14. sudo timedatectl set-timezone America/Los_Angeles
15. sudo scp -r /etc/letsencrypt root@137.184.176.40:/etc/




1. Если виртуалка новая, тогда чтобы выполнить команду git clone, необходимо сгенерить новый ключ `ssh-keygen -t rsa -b 4096 -C "vladismeno@gmail.com"`
2. Берем ключ `cat ~/.ssh/id_rsa.pub` и добавляем его в git, там где лежит наш проект
3. Клонировать репозиторий: `git clone git@github.com:vladismeno/cleanhouse.git`
4. sh install_docker.sh



root@cleanhouse:~# docker --version
Docker version 27.3.1, build ce12230



ВОТ ТАК ВЫГЛЯДИТ ЛОГ, ЕСЛИ УСПЕШНОСТАРТОВАЛ NGINX И DJANGO
✔ Network cleanhouse_default  Created                                                                                                                                                                 0.1s
 ✔ Container django            Created                                                                                                                                                                 0.1s
 ✔ Container nginx             Created                                                                                                                                                                 0.0s
Attaching to django, nginx
django  | 2024-11-20 02:25:58,006 INFO Set uid to user 0 succeeded
django  | 2024-11-20 02:25:58,014 INFO supervisord started with pid 1
nginx   | 2024-11-20 02:25:58,257 INFO Set uid to user 0 succeeded
nginx   | 2024-11-20 02:25:58,261 INFO supervisord started with pid 1
django  | 2024-11-20 02:25:59,021 INFO spawned: 'django' with pid 7
nginx   | 2024-11-20 02:25:59,266 INFO spawned: 'nginx' with pid 9
nginx   | 2024-11-20 02:26:00,271 INFO success: nginx entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)
django  | 2024-11-20 02:26:00,301 INFO success: django entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)



Если делаем ping cleanhouse4you.com
а пингует старый ip
неоюходимо выполнить
sudo killall -HUP mDNSResponder





