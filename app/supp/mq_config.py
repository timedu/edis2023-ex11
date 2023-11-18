
import paho.mqtt.client as mqtt # pyright: ignore
from os import environ
from time import sleep


MQ_TOPIC = f"/edis/{ environ.get('HOSTNAME')}"
MQ_PUBLISH_DELAY = 0.2


_MQTT_BROKER_URL = 'mqtt-container'

def connect():
    mq_client = mqtt.Client()
    mq_client.connect(_MQTT_BROKER_URL, 1883, 60)
    mq_client.loop_start()
    return mq_client

def disconnect(mq_client):
    mq_client.loop_stop()
    mq_client.disconnect()



_NO_MESSAGES_TIMEOUT = 5
_no_messages_counter = 0

def is_time_to_wait():
    global _no_messages_counter
    sleep(1)
    _no_messages_counter += 1
    return _no_messages_counter <  _NO_MESSAGES_TIMEOUT
  
def reset_time_to_wait():
    global _no_messages_counter
    _no_messages_counter = 0
