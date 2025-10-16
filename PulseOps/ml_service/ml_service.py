import pika
import redis
import os
import time
import json
import random

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "tasks")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

# Connect to Redis
r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=RABBITMQ_QUEUE)

def process_task(task):
    # Simulate processing delay
    time.sleep(random.uniform(1, 3))  # 1-3 seconds per task
    result = {"task": task, "status": "processed"}
    return result

def callback(ch, method, properties, body):
    task = body.decode()
    print(f"[ML Service] Processing task: {task}")
    result = process_task(task)
    r.set(f"task:{task}", json.dumps(result))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)

print("[ML Service] Waiting for tasks...")
channel.start_consuming()
