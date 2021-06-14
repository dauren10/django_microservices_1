#amqps://qlcexzxa:iFceMBpIaMuHMyDMYNNPFtiy9GRhNmOD@goose.rmq2.cloudamqp.com/qlcexzxa
import pika, json

params = pika.URLParameters('amqps://qlcexzxa:iFceMBpIaMuHMyDMYNNPFtiy9GRhNmOD@goose.rmq2.cloudamqp.com/qlcexzxa')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method=None, body=None):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)