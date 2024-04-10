FROM python:latest
RUN apt-get update -y && rm -rf /var/lib/apt/lists/* \
  && echo "alias l='ls -lah --color=auto'" >> ${HOME}/.profile
WORKDIR /app
# ADD ./app/* .
ADD ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
