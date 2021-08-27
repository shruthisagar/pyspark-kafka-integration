## This is readme file to run this demo. This has steps to run each command

**_Connecting Spark, Kafka using python_**
Tutorials used

- [Link 1](https://towardsdatascience.com/connecting-the-dots-python-spark-and-kafka-19e6beba6404)

Steps:

- cd spa/kafka/kafka
- starting zookeeper
  - sh bin/zookeeper-server-start.sh config/zookeeper.properties
- starting brokers
  - ./bin/kafka-server-start.sh config/server.properties
  - ./bin/kafka-server-start.sh config/server1.properties
- creating topic

  - bin/kafka-topics.sh --create --zookeeper localhost:2181 --topic kafka-spark --replication-factor 2 --partitions 2
  - here kafka-spark is the topic i have created replication factor is 2 because there are 2 brokers

- describing a topic

  - bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic kafka-spark

- coding for kafka-spark.py

  - command to run kafka-spark.py
    - spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.0 kafka-spark.py
