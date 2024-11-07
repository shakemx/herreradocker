FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir assets
COPY ./staticfiles /assets
COPY nginx.conf /etc/nginx/conf.d