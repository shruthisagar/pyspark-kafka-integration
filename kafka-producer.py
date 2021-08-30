import csv

csv_data = csv.DictReader(open("./user_posts.csv"))
posts_data = []
for i in csv_data:
    posts_data.append(i)
from kafka import KafkaProducer
from datetime import datetime
import time
from json import dumps

KAFKA_TOPIC = "kafka-spark"
KAFKA_SERVER = "localhost:9092"

if __name__ == "__main__":
    kafka_producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, value_serializer=lambda m: dumps(m).encode('ascii'))
    for i in posts_data:
        print(i)
        kafka_producer.send(topic=KAFKA_TOPIC, key=dumps(i).encode("utf-8"), value=i)
        time.sleep(1)