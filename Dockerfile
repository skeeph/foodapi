FROM python:3.6-slim

RUN mkdir /opt/app
RUN apt-get update && apt-get install -y build-essential netcat nginx
ADD requirements.txt /opt/app
COPY requirements /opt/app/requirements

RUN cd /opt/app && pip install -r requirements.txt && pip install uwsgi
RUN apt-get purge -y build-essential && apt-get autoremove -y

ADD . /opt/app


WORKDIR /opt/app