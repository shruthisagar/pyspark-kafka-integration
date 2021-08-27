from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('kafka-spark', bootstrap_servers=['127.0.0.1:9092'])
for i in consumer:
    data = json.loads(i.value)
    import os
    import csv
    from datetime import datetime
    print("hello i am in pyspakr")
    if not os.path.exists("./login.csv"):
        with open('login.csv', mode='w') as csv_file:
            fieldnames = ['user_name', 'login_time']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'user_name': data.get("user_name"), 'login_time': datetime.utcnow()})
    else:
        with open('login.csv', mode='a') as csv_file:
            fieldnames = ['user_name', 'login_time']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'user_name': data.get("user_name"), 'login_time': datetime.utcnow()})
