FROM nginx:1.19.8-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./conf.d/nginx.conf /etc/nginx/conf.d
COPY ./nginx.conf /etc/nginx/
COPY /app/cleanhouse4you.com/ /etc/letsencrypt/live/cleanhouse4you.com/