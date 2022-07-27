FROM python:latest

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD python3 app.py
