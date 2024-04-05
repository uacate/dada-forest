FROM python:latest
RUN apt-get update -y
WORKDIR /src/app
ADD ./app/* .
ADD ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
