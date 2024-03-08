FROM python:latest
ENV PYTHONBUFFERED=1
RUN apt-get update && apt-get install build-essential && \
    pip install --no-cache-dir pipenv && \
    pip install pip --upgrade && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /usr/dada-forest
COPY Pipfile ./Pipfile
COPY Pipfile.lock ./Pipfile.lock
RUN pipenv install --dev --system --deploy