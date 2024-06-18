# Используем образ Python с установленным Django
FROM python:3.12

# Установка переменной среды для запуска в неинтерактивном режиме
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Создание директории для кода проекта и установка рабочей директории
RUN mkdir /app
WORKDIR /app

# Копирование файла зависимостей и установка их
COPY requirements.txt /app/
RUN pip install -r requirements.txt

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf", "-n"]
