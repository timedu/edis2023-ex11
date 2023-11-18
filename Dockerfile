FROM python:3.9-slim
WORKDIR /home/app
RUN pip install --no-cache-dir paho-mqtt
