FROM python:3.6-stretch

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y nano htop
RUN pip install -r requirements.txt
