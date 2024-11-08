FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir static
COPY ./staticfiles /static
COPY nginx.conf /etc/nginx/conf.d
