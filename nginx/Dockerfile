FROM nginx:1.19.8-alpine

RUN apk update && apk add --no-cache supervisor


RUN rm /etc/nginx/conf.d/default.conf
COPY ./conf.d/nginx.conf /etc/nginx/conf.d
COPY ./nginx.conf /etc/nginx/

CMD ["supervisord", "-n"]