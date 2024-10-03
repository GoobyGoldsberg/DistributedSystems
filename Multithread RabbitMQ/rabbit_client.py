import pika

# RabbitMQ configuration
rabbitmq_host = 'localhost'
rabbitmq_port = 5672
rabbitmq_exchange = 'activity_logs'

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode('utf-8')}")

def consume_activity_logs():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
    channel = connection.channel()
    channel.exchange_declare(exchange=rabbitmq_exchange, exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange=rabbitmq_exchange, queue=queue_name)

    print('Waiting for activity logs. To exit press Ctrl+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == "__main__":
    consume_activity_logs()