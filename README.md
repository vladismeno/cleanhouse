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
16. **letsencrypt** - это бесплатный и автоматизированный центр сертификации, который предоставляет SSL/TLS сертификаты
17. **сertbot** - это инструмент для работы с Let's Encrypt (установки и автоматического обновления сертификатов)

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

### этот шаблон я использовал для сайта
https://themewagon.com/themes/free-bootstrap-4-html5-business-website-template-cleaning-company/

## КАК РАЗВЕРНУТЬ ПРОЕКТ

Django не обслуживает статические файлы автоматически. Для того чтобы статические файлы работали при локальной 
разработке с DEBUG = False, необходимо настроить статический сервер, такой как WhiteNoise, или использовать другой 
веб-сервер, например, Nginx или Apache.
Если локально не отображаются статические файлы, тогда необходимо включить DEBUG = True
Проверить занят ли порт lsof -nP -iTCP -sTCP:LISTEN | grep "443"

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

### ДЕПЛОЙ ПРОЕКТА НА DIGITAL OCEAN

1. **Логинимся в Digital Ocean**  
   Переходим на [Digital Ocean](https://cloud.digitalocean.com/login) и входим с помощью почты Наташи.

2. **Создаем Droplet**
   - Создаем Droplet за $4/месяц.
   - Выбираем вход по **паролю** (при выборе SSH-ключа команда `scp` может не работать).
   - Сохраняем выбранный пароль.

3. **Настраиваем DNS**
   - Переходим на [Squarespace DNS](https://account.squarespace.com/domains/managed/cleanhouse4you.com/dns/dns-settings).
   - Прописываем IP Droplet в настройках DNS.
     - Актуальные настройки в файле `dns3.png`.
     - Исторические настройки сохранены в файлах `dns1.png` и `dns2.png`.

4. **Подключаемся к серверу**
   - Подключаемся к серверу по SSH:
     ```bash
     ssh root@cleanhouse4you.com or ssh root@<ip_droplet>
     ```
   - Если не удается подключиться:
     - Очистите запись в `known_hosts`:
       ```bash
       vim /Users/svs/.ssh/known_hosts
       ```
       Удалите все строки с `cleanhouse4you.com`. 

5. **Создаем сеанс `screen`**
   - Запускаем новый сеанс:
     ```bash
     screen
     ```

6. **Настраиваем временную зону**
   - Устанавливаем временную зону на сервере:
     ```bash
     sudo timedatectl set-timezone America/Los_Angeles
     ```

7. **Генерируем SSH-ключ (для новой виртуалки)**
   - Генерируем новый SSH-ключ:
     ```bash
     ssh-keygen -t rsa -b 4096 -C "vladismeno@gmail.com"
     ```
   - Просматриваем ключ:
     ```bash
     cat ~/.ssh/id_rsa.pub
     ```
   - Добавляем ключ в Git-репозиторий.

8. **Клонируем репозиторий**
   - Клонируем проект в директорию `/root/cleanhouse`:
     ```bash
     git clone git@github.com:vladismeno/cleanhouse.git
     ```

9. **Устанавливаем Docker и Make**
   - Выполняем скрипт установки:
     ```bash
     sh /root/cleanhouse/scripts/install_docker.sh
     ```
   - Чтобы убедиться, что докер нужной версии:
     ```bash
     root@cleanhouse:~# docker --version
     Docker version 27.3.1, build ce12230   
     ```

10. **Создаем файл `.env`**
    - Создаем `.env` файл в корне проекта:
      ```bash
      vim /root/cleanhouse/.env
      ```
    - Добавляем следующие строки:
      ```env
      DEBUG=True
      SECRET_KEY='django-insecure-8q^tpixw1go4@uk5a6q0s7+*b)(tltvi^b**%cffzhmm54lef#'
      ALLOWED_HOSTS='localhost,127.0.0.1,0.0.0.0,192.168.1.108,137.184.176.40,cleanhouse4you.com,www.cleanhouse4you.com'
      ```

11. **Передаем SSL-сертификаты**
    - С локальной машины на сервер:
      ```bash
      sudo scp -r /etc/letsencrypt root@<ip_droplet>:/etc/
      ```
    - Или локально копируем содержимое сертификатов:
      ```bash
      cp -r /root/cleanhouse/letsencrypt /etc/
      ```

12. **Запускаем проект**
    - Поднимаем проект:
      ```bash
      make up
      ```

13. **Собираем статические файлы**
    - Выполняем команду:
      ```bash
      make collectstatic
      ```

14. **Применяем миграции, скорей всего эта команда не нужна, так как данные хранятся в cleanhouse.sqlite3, ну пусть будет**
    - Выполняем команду:
      ```bash
      make migrate
      ```

15. **Создаем, если нужно суперпользователя Django, чтобы можно было добавлять коменты в админке**:
    - Выполняем команду:
      ```bash
      make createsuperuser
      ```
    - Вообще по умолчанию есть пользователь с логином root и паролем 111
    - Чтобы добавить новые комменты, нужно зайти по адресу https://cleanhouse4you.com/admin/

16. **Обновляем или пересоздаем сертификат SSL**
    - Выполняем скрипт обновления:
      ```bash
      sh /root/cleanhouse/scripts/update_certificate.sh
      ```
      - Если обновить сертификат не удалось, то необходимо создать заново сертификат. Выполняем следующие шаги:
      16.1. Удаляем все файлы в этих директориях:
        `sudo rm -rf /etc/letsencrypt/accounts/
        sudo rm -rf /etc/letsencrypt/live/
        sudo rm -rf /etc/letsencrypt/renewal/
        sudo rm -rf /etc/letsencrypt/archive/`
      16.2. Создаем заново сертификат
        `sh /root/cleanhouse/scripts/create_certificate.sh`
      16.3. После создания сертификата должно получится вот так:
        `root@cleanhouse:/etc/letsencrypt/live/cleanhouse4you.com# ls -n
        total 4
        -rw-r--r-- 1 0 0 692 Nov 21 11:59 README
        lrwxrwxrwx 1 0 0  42 Nov 21 11:59 cert.pem -> ../../archive/cleanhouse4you.com/cert1.pem
        lrwxrwxrwx 1 0 0  43 Nov 21 11:59 chain.pem -> ../../archive/cleanhouse4you.com/chain1.pem
        lrwxrwxrwx 1 0 0  47 Nov 21 11:59 fullchain.pem -> ../../archive/cleanhouse4you.com/fullchain1.pem
        lrwxrwxrwx 1 0 0  45 Nov 21 11:59 privkey.pem -> ../../archive/cleanhouse4you.com/privkey1.pem`
      16.4. Если проект не работает, то останавливаем проект  `make down` и стартуем заново `make up` и должно все заработать
      16.5. Вот так выглядит лог, если проект успешно стартовал
         `
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
        django  | 2024-11-20 02:26:00,301 INFO success: django entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)`
      16.6. Вот так выглядит лог если сертификат успешно обновился
        `
            sh /root/cleanhouse/scripts/update_certificate.sh
            Saving debug log to /var/log/letsencrypt/letsencrypt.log
            Processing /etc/letsencrypt/renewal/cleanhouse4you.com.conf
            Renewing an existing certificate for cleanhouse4you.com
            Congratulations, all renewals succeeded:
            /etc/letsencrypt/live/cleanhouse4you.com/fullchain.pem (success)
            [+] Restarting 1/1
            ✔ Container nginx  Started
        `     
        ` 
            root@cleanhouse:/etc/letsencrypt/live/cleanhouse4you.com# ls -n
            total 4
            -rw-r--r-- 1 0 0 692 Nov 21 11:59 README
            lrwxrwxrwx 1 0 0  42 Nov 21 13:45 cert.pem -> ../../archive/cleanhouse4you.com/cert2.pem
            lrwxrwxrwx 1 0 0  43 Nov 21 13:45 chain.pem -> ../../archive/cleanhouse4you.com/chain2.pem
            lrwxrwxrwx 1 0 0  47 Nov 21 13:45 fullchain.pem -> ../../archive/cleanhouse4you.com/fullchain2.pem
            lrwxrwxrwx 1 0 0  45 Nov 21 13:45 privkey.pem -> ../../archive/cleanhouse4you.com/privkey2.pem
        `
17. ** Добавляем в крон обновление сертификата 1 раз в месяц первого числа**
        `crontab -e
         0 0 1 * * /root/cleanhouse/scripts/update_certificate.sh >> /var/log/update_certificate.log 2>&1
        `
        Возможно нужно будет проставить права на файл
        `chmod +x /root/cleanhouse/scripts/update_certificate.sh`
        Вот здесь можно смотреть лог, выполнился крон или нет
        `tail -f /var/log/update_certificate.log`

        Если нужно будет посмотреть лог выполнения крона
        `root@cleanhouse:/etc/letsencrypt/renewal# tail -f /var/log/update_certificate.log
        Processing /etc/letsencrypt/renewal/cleanhouse4you.com.conf
        Renewing an existing certificate for cleanhouse4you.com
        Congratulations, all renewals succeeded:
        /etc/letsencrypt/live/cleanhouse4you.com/fullchain.pem (success)
        Container nginx  Restarting
        Container nginx  Started`

 


### ШПАРГАЛКА ПО ОБЩИМ ПРОБЛЕМАМ С ПРОЕКТОМ
1. Если делаем `ping cleanhouse4you.com`, а пингует старый ip, необходимо выполнить: `sudo killall -HUP mDNSResponder`
2. Если не запускается nginx, или запускается, но правильно не работает, здесь можем посмотреть ошибки
```
docker exec -it nginx tail -f /var/log/supervisor/nginx.log
docker exec -it nginx tail -f /var/log/supervisor/nginx_err.log
stdout_logfile=/var/log/supervisor/nginx.log
stderr_logfile=/var/log/supervisor/nginx_err.log

docker exec -it django tail -f /var/log/supervisor/django.log
docker exec -it django tail -f /var/log/supervisor/django_err.log
stdout_logfile=/var/log/supervisor/django.log
stderr_logfile=/var/log/supervisor/django_err.log
```
