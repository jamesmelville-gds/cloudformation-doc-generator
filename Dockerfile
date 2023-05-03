FROM python:3.8-slim AS compile

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
ENV PATH='/opt/venv/bin:$PATH'

WORKDIR /usr/src/app
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install gunicorn

# To match the directory structure at host:
ADD src/ ./src
ADD setup.py .
RUN pip install .