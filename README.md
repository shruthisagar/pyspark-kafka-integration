# This is readme file to run this demo. This has steps to run each command

## Connecting Spark, Kafka using python

### Tutorials used

- [Link 1](https://towardsdatascience.com/connecting-the-dots-python-spark-and-kafka-19e6beba6404)
- [Link 2](https://www.youtube.com/watch?v=zVgPNjSjua0)

Steps:

- Install Kafka as in this [Link](https://towardsdatascience.com/quickstart-apache-kafka-kafka-python-e8356bec94)

- I have my kafka server running in the directory **kafka_server**

- cd kafka_server

- **All these commands are to be run in the directory where your Kafka server is saved. *kafka_server* in my case**

- starting zookeeper
  - sh ./bin/zookeeper-server-start.sh config/zookeeper.properties

- starting brokers
  - ./bin/kafka-server-start.sh config/server.properties
  - ./bin/kafka-server-start.sh config/server1.properties

- creating topic
  - ./bin/kafka-topics.sh --create --topic kafka-spark  --bootstrap-server localhost:9092 --replication-factor 2 --partitions 2
  - here kafka-spark is the topic i have created replication factor is 2 because there are 2 brokers

- listing topics
  - ./bin/kafka-topics.sh --list --bootstrap-server localhost:9092 localhost:2181

- describing a topic
  - ./bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic kafka-spark

- creating prodcer for sending messages
  - ./bin/kafka-console-producer.sh  --broker-list localhost:9092 --topic kafka-spark

- listening to a producer as a consumer
  - ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic kafka-spark --from-beginning
KV
- deleting a topic
  - ./bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic kafka-spark

### Spark

Setting up enviornment variables

``` sh
  SPARK_HOME="/home/xxx/kafka_pyspark/spark"
  export PATH=$SPARK_HOME/bin:$PATH
  export PATH=$SPARK_HOME/sbin:$PATH
```

Validate installation using

```sh
  pyspark
```

Start the Spark server

```sh
  start-master.sh
```

Export spark env

```sh
   export PYSPARK_PYTHON='/home/xxx/kafka_pyspark/env/bin/python'
```

- coding for kafka-spark.py

  - command to run kafka-spark.py

  ```sh
    - spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.12:2.0.0 consumer1.py
    - spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 streamer.py
    - curl -d "hello world" -H "Content-Type: application/json" -X POST <http://localhost:5000/>
  ```
