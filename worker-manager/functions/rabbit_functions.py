import pika,os


# connect to rabbit function
def rabbit_connect(rabbit_user, rabbit_pass, rabbit_host, rabbit_port, rabbit_virtual_host):
    try:
        credentials = pika.PlainCredentials(rabbit_user, rabbit_pass)
        connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_host, rabbit_port, rabbit_virtual_host, credentials, heartbeat_interval=0))
        return connection
    except:
        os._exit(2)


# close connection to rabbit function
def rabbit_close(rabbit_connection):
    try:
        rabbit_connection.close()
    except:
        os._exit(2)


# create channel
def rabbit_create_channel(rabbit_connection):
    try:
        channel = rabbit_connection.channel()
        return channel
    except:
        os._exit(2)


# create exchange
def rabbit_create_exchange(rabbit_channel, exchange_name):
    try:
        rabbit_channel.exchange_declare(exchange=exchange_name, type='fanout')
    except:
        os._exit(2)


# send message
def rabbit_send(rabbit_channel, exchange_name, rabbit_send_message):
    try:
        rabbit_channel.basic_publish(exchange=exchange_name, routing_key='', body=rabbit_send_message)
    except:
        os._exit(2)


# receive message
def rabbit_receive(rabbit_receive_channel, rabbit_work_function, rabbit_receive_queue):
    try:
        rabbit_receive_channel.basic_consume(rabbit_work_function, queue=rabbit_receive_queue)
        rabbit_receive_channel.start_consuming()
    except:
        os._exit(2)


# ack message
def rabbit_ack(rabbit_ack_channel, rabbit_ack_method):
    try:
        rabbit_ack_channel.basic_ack(delivery_tag=rabbit_ack_method.delivery_tag)
    except:
        os._exit(2)


# create queue
def rabbit_create_queue(rabbit_queue_name, rabbit_channel):
    try:
        created_queue = rabbit_channel.queue_declare(queue=rabbit_queue_name, arguments={"x-expires": 300000})
        return created_queue
    except:
        os._exit(2)


# bind queue to exchange
def rabbit_bind_queue(rabbit_bind_queue_name, rabbit_bind_channel, rabbit_bind_exchange):
    try:
        rabbit_bind_channel.queue_bind(exchange=rabbit_bind_exchange, queue=rabbit_bind_queue_name)
    except:
        os._exit(2)
