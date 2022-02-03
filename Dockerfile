FROM python:3.9-slim
RUN pip3 install --upgrade pip
RUN pip3 install bme680 flask

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .

CMD python3 main.py
