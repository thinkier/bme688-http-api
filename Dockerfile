FROM python:3.9-slim
WORKDIR /app
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip3 install bme680 flask
COPY . .

CMD python3 main.py
