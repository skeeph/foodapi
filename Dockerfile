FROM python:3.6-slim

RUN mkdir /opt/app
RUN apt-get update && apt-get install -y build-essential nginx aria2 netcat
ADD requirements.txt /opt/app
COPY requirements /opt/app/requirements

RUN cd /opt/app && pip install -r requirements.txt \
                && pip install uwsgi \
                && pip install -r requirements/test.txt

RUN apt-get purge -y build-essential && apt-get autoremove -y
RUN ln -s /opt/app/api_nginx.conf /etc/nginx/sites-enabled/

RUN mkdir -p /opt/app/frontend && mkdir -p /opt/app/statics

RUN cd /opt/app/frontend \
        && aria2c "https://khabib.me/menu.tar.gz"\
        && tar -xvf menu.tar.gz\
        && mv dist/* . \
        && rm menu.tar.gz \
        && rm -rf dist
RUN apt-get install -y ssh
ADD . /opt/app

RUN python /opt/app/api/manage.py collectstatic --no-input


WORKDIR /opt/app