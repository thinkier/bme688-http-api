FROM python:3.9-buster
WORKDIR /app
ENV PYTHONUNBUFFERED 1

RUN pip3 install bme680 flask
COPY . .

CMD python3 main.py
