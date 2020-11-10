FROM tiangolo/uwsgi-nginx:python3.8-alpine
LABEL Author="Jino PL"

RUN pip3 install flask

COPY ./app /app