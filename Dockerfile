FROM ubuntu:bionic
LABEL Author="Jino PL"

RUN apt-get update && apt-get install nginx -y


RUN  apt-get install -y python3 python3-pip python3-dev gunicorn && \
    pip3 install --no-cache-dir flask setuptools && \
    apt-get remove python3-pip -y && \
    apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY . /var/www/html/

