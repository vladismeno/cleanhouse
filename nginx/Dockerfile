FROM nginx:1.19.8

RUN apt-get update && apt-get install -y supervisor

WORKDIR /app

RUN rm /etc/nginx/conf.d/default.conf

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./conf.d/nginx.conf /etc/nginx/conf.d
COPY ./nginx.conf /etc/nginx/
COPY ./robots.txt /app/robots.txt
COPY ./404.html /app/404.html

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf", "-n"]