### Деплой проекта на Digital Ocean

1. **Логинимся в Digital Ocean**  
   Переходим на [Digital Ocean](https://cloud.digitalocean.com/login) и входим с помощью почты.

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

14. **Обновляем сертификат**
    - Выполняем скрипт обновления:
      ```bash
      sh /root/cleanhouse/scripts/update_certificate.sh
      ```
