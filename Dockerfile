FROM tiangolo/uwsgi-nginx-flask:flask
MAINTAINER Chris Sterling "csterling@newmediadenver.com"
COPY ./app /app
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
WORKDIR /app
ENV NEW_RELIC_LICENSE_KEY=927860b54a65a296846de0b863c6665845ea2416
# MongoDB
RUN mkdir -p /data/db/
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list
RUN apt-get update
RUN apt-get -y install nginx-nr-agent vim mongodb-org
RUN pip install -r requirements.txt