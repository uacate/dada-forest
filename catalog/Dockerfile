FROM python:latest
RUN apt-get update -y && apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /catalog
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# # Using ubuntu LTS version
# FROM ubuntu:20.04 AS builder-image

# RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
#    apt-get clean && rm -rf /var/lib/apt/lists/*

# # create and activate virtual environment
# RUN python3.9 -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"

# # install requirements
# COPY requirements.txt .
# RUN pip3 install --no-cache-dir -r requirements.txt

# FROM ubuntu:20.04 AS runner-image
# RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3-venv && \
#    apt-get clean && rm -rf /var/lib/apt/lists/*

# COPY --from=builder-image /opt/venv /opt/venv

# # activate virtual environment
# ENV VIRTUAL_ENV=/opt/venv
# ENV PATH="/opt/venv/bin:$PATH"

# CMD ["python"]