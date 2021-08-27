from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
def kafka_send_data(data):
    
    res = producer.send('kafka-spark', data)
    producer.flush()
    # logic to send to db can be written here