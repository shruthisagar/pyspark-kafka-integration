from random import random
import hashlib
from kafka import KafkaProducer

topic = 'kontext-kafka'
bootstrap_servers = 'localhost:9092'

def hash_partitioner(key, all_partitions, available):
    """
    Customer Kafka partitioner to get the partition corresponding to key
    :param key: partitioning key
    :param all_partitions: list of all partitions sorted by partition ID
    :param available: list of available partitions in no particular order
    :return: one of the values from all_partitions or available
    """

    if key is None:
        if available:
            return random.choice(available)
        return random.choice(all_partitions)

    idx = int(hashlib.sha1(key).hexdigest(), 16) % (10 ** 8)
    idx &= 0x7fffffff
    idx %= len(all_partitions)
    return all_partitions[idx]

producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         partitioner=hash_partitioner)
# Generate 100 messages
for _ in range(200, 300):
    msg = f'Kontext kafka msg: {_}'
    future = producer.send(topic, value=msg.encode('utf-8'),
                           key='cba'.encode('utf8'))
    print(f'Sending msg: {msg}')
    result = future.get(timeout=60)