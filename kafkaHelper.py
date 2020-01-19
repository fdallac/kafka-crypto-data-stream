import time
import numpy as np

from kafka import KafkaProducer, KafkaConsumer
from config import config


def initProducer():
    # init an instance of KafkaProducer
    print('Initializing Kafka producer at {}'.format(time.time()))
    producer = KafkaProducer(bootstrap_servers=config['kafka_broker'])
    print('Initialized Kafka producer at {}'.format(time.time()))
    return producer


def initConsumer(topic, timeout=1000):
    # init an instance of KafkaConsumer
    consumer = KafkaConsumer(topic, bootstrap_servers=config['kafka_broker'], group_id=None,
        auto_offset_reset='earliest', enable_auto_commit=False, consumer_timeout_ms=timeout)
    return consumer


def produceRecord(data, producer, topic, partition=0):
    # act as a producer sending records on kafka
    producer.send(topic=topic, partition=partition, value=bytes(str(data), 'utf-8'))
    # debug \ message in prompt
    # print('Produce record to topic \'{0}\' at time {1}'.format(topic, time.time()))
    
import ast

def consumeRecord(consumer):
    rec_list = []
    # append to list any new records in consumer
    for rec in consumer:
        r = rec.value.decode('utf-8')
        rec_list.append(ast.literal_eval(r))
    # return list of new records
    return rec_list