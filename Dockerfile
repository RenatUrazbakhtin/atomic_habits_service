FROM python:3

WORKDIR /app

COPY ./requirements /app/

RUN pip install -r /app/requirements

COPY . .