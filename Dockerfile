FROM python:3.8-slim AS compile

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
ENV PATH='/opt/venv/bin:$PATH'

WORKDIR /usr/cloudformation_docs/cli
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# To match the directory structure at host:
ADD cloudformation_docs/ ./cloudformation_docs
ADD README.md .
ADD setup.py .
RUN pip install .