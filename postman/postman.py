#!/usr/bin/env python
import pika
import time
import mandrill
import json

mandrill_client = mandrill.Mandrill('U9hPDmidFONYzIVg_hWfuw')
credentials = pika.PlainCredentials('guest', 'guest')
cn = pika.BlockingConnection(
    pika.ConnectionParameters(
        '127.0.0.1',
        5672,
        '/',
        credentials
    )
)
channel = cn.channel()
channel.queue_declare(queue='email_queue')
print '[*] Waiting for message. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print "[x] Received: %r" %(body,)
    decoded_body = json.load(body)
    print decoded_body
    msg = {
        'to':           [{'email': decoded_body['email']}],
        'text':         decoded_body['content'],
        'from_email':   'janusz.biznesu@handlarze.pl'
    }

    result = mandrill_client.messages.send(
        message = msg, async=False, ip_pool='Main Pool'
    )
    print result
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='email_queue',
                      no_ack=False) # kolejka zostanie powiadomiona i po jakims czasie zostanie ponownie wyslana
channel.start_consuming()
