FROM nginx:1.19.8-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./conf.d/nginx.conf /etc/nginx/conf.d
COPY ./nginx.conf /etc/nginx/
RUN chmod -R 755 /etc/letsencrypt/live/cleanhouse4you.com/
COPY /etc/letsencrypt/live/cleanhouse4you.com/ /etc/letsencrypt/live/cleanhouse4you.com/