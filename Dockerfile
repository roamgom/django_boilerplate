FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

# web_app directory 추가
ADD . /web_app
# Django source file copy & change work directory
COPY . /web_app
WORKDIR /web_app


RUN pip install -r requirements.txt

EXPOSE 8080

# env variables
# ENV DB_URL mysql