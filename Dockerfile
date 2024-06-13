# Используем образ Python с установленным Django
FROM python:3.12-alpine

# Установка переменной среды для запуска в неинтерактивном режиме
ENV PYTHONUNBUFFERED 1

RUN apk update && apk install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Создание директории для кода проекта и установка рабочей директории
RUN mkdir /app
WORKDIR /app

# Копирование файла зависимостей и установка их
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Копирование всего остального в рабочую директорию
COPY . /app/

CMD ["supervisord", "-n"]
