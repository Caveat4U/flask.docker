FROM tiangolo/uwsgi-nginx-flask:flask
MAINTAINER Chris Sterling "csterling@newmediadenver.com"
COPY ./app /app
WORKDIR /app
RUN apt-get update
RUN apt-get -y install mongodb mongodb-server mongodb-clients
RUN pip install -r requirements.txt
