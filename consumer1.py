import os

os.environ["PYSPARK_PYTHON"] = "/home/sscr/spa/6env/bin/python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "/home/sscr/spa/6env/bin/python"

from flask import Flask, json, request, jsonify
import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext(appName="kafka demo")
ssc = StreamingContext(sc, 30)
message = KafkaUtils.createDirectStream(ssc, topics=['kafka-spark'],
            kafkaParams={"metadata.broker.list":"localhost:9092"})
data = json.loads(message)
print(data)
words = message.map(lambda x:x[1]).flatMap(lambda x: x.split(" "))
wordcount = words.map(lambda x:(x,1)).reduceByKey(lambda a,b: a+b)


import pprint
import io
wordcount.pprint()
f = io.StringIO()
pprint.pprint(wordcount, f) # note: pass d and not dict
f.seek(0) # move pointer to start of file
res = f.read()
print(res)
f = open("finaldata.txt", "a")
f.write(res)
f.close()
ssc.start()
ssc.awaitTermination()