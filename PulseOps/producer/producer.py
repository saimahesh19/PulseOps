# import os
# import time
# import json
# import pika
# import random

# RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'rabbitmq')
# QUEUE = os.environ.get('RABBITMQ_QUEUE', 'tasks')

# # Retry until RabbitMQ is ready
# while True:
#     try:
#         connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
#         break
#     except pika.exceptions.AMQPConnectionError:
#         print("Waiting for RabbitMQ...")
#         time.sleep(5)

# channel = connection.channel()
# channel.queue_declare(queue=QUEUE)

# print("Producer started...sending tasks")

# while True:
#     task = {
#         "id": random.randint(1000, 9999),
#         "value": random.randint(1, 100)
#     }
#     channel.basic_publish(exchange='', routing_key=QUEUE, body=json.dumps(task))
#     print(f"Sent task: {task}")
#     time.sleep(1)

import os, time, json, pika, random

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'rabbitmq')
QUEUE = os.environ.get('RABBITMQ_QUEUE', 'tasks')

while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
        break
    except pika.exceptions.AMQPConnectionError:
        print("Waiting for RabbitMQ...")
        time.sleep(5)

channel = connection.channel()
channel.queue_declare(queue=QUEUE)

while True:
    task = {"id": random.randint(1000,9999), "value": random.randint(1,100)}
    channel.basic_publish(exchange='', routing_key=QUEUE, body=json.dumps(task))
    print(f"Sent task: {task}")
    time.sleep(1)
