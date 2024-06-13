FROM nginx:1.19.8-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./conf.d/nginx.conf /etc/nginx/conf.d
COPY ./nginx.conf /etc/nginx/
COPY ./cleanhouse4you.com/cert.pem /etc/letsencrypt/live/cleanhouse4you.com/cert.pem
COPY ./cleanhouse4you.com/chain.pem /etc/letsencrypt/live/cleanhouse4you.com/chain.pem
COPY ./cleanhouse4you.com/fullchain.pem /etc/letsencrypt/live/cleanhouse4you.com/fullchain.pem
COPY ./cleanhouse4you.com/privkey.pem /etc/letsencrypt/live/cleanhouse4you.com/privkey.pem