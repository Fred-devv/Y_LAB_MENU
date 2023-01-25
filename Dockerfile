FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade setuptools 

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY . ./app

EXPOSE 8000
