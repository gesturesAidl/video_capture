import os
import pika
from typing import Optional
import uuid

from gesturesApp.app.config.constants.RabbitConstants import RabbitConstants


class RabbitTemplate:
    RABBIT_USER: Optional[str]
    RABBIT_PW: Optional[str]
    RABBIT_HOST: Optional[str]
    RABBIT_PORT: Optional[int]

    def __init__(self):
        self.load_env()
        credentials = pika.PlainCredentials(self.RABBIT_USER, self.RABBIT_PW)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.RABBIT_HOST, port=int(self.RABBIT_PORT), credentials=credentials))
        self.channel = self.connection.channel()

        self.result = self.channel.queue_declare(queue=RabbitConstants.RPC_REP_QUEUE, exclusive=True)
        self.callback_queue = self.result.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    # .env vars
    def load_env(self):
        self.RABBIT_USER = os.getenv('RABBIT_USER')
        self.RABBIT_PW = os.getenv('RABBIT_PW')
        self.RABBIT_HOST = os.getenv('RABBIT_HOST')
        self.RABBIT_PORT = os.getenv('RABBIT_PORT')

    def publish_video(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange=RabbitConstants.RPC_DIRECT_EXCHANGE,
            routing_key=RabbitConstants.RPC_REQ_ROUTING_KEY,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=n)
        while self.response is None:
            self.connection.process_data_events()
        return print(self.response)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body