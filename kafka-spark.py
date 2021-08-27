import os

os.environ["PYSPARK_PYTHON"] = "/home/sscr/spa/6env/bin/python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "/home/sscr/spa/6env/bin/python"

from flask import Flask, json, request, jsonify
import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from producer import kafka_send_data

app = Flask(__name__)
@app.route("/", methods=["POST"])
def send_data():
    data = request.data
    kafka_send_data(data)
    return jsonify({"status": 1})

if __name__ == "__main__":
    
    
    app.run(debug=True)

