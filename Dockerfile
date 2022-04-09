FROM bitnami/minideb:stretch
LABEL Author="JINO"

RUN install_packages nginx python3 python3-pip && \
    pip3 install flask && \
    apt-get remove --purge python3-pip -y && \
    mkdir -p /app

COPY /app/ /app
WORKDIR /app
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
EXPOSE 8080
ENTRYPOINT ["python3", "catsnation.py"]