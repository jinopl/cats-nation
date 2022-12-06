FROM python:3.7.15-alpine

WORKDIR /code

RUN pip install --no-cache-dir gunicorn flask

COPY ./app /code/


RUN ls -la

CMD ["gunicorn", "--conf", "gunicorn_conf.py", "--bind", "0.0.0.0:8080", "wsgi:app"]