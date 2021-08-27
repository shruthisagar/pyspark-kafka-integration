from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

res = producer.send('kafka-spark', b'Hey yaako')

producer.flush()