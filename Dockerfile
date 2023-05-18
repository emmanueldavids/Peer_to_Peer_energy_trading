FROM python:3.12.0a7-slim

LABEL p2p-energy-trading.image.authors="< emmanueldavids417@gmail.com >: < hledavids@gmail.com >"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip

RUN pip install setuptools

RUN pip3 install -r /requirements.txt

RUN mkdir /app

WORKDIR /app

COPY ./Future_Of_Energy /app

RUN adduser --disabled-password user

USER user
