import rabbitpy

with rabbitpy.Connection('amqp://guest:guest@localhost:5672/%2f') as conn:
    with conn.channel() as channel:
        queue = rabbitpy.Queue(channel, 'example')
        queue.declare()
        queue.bind('test_exchange')
        
        # Exit on CTRL-C
        try:
            # Consume the message
            for message in queue:
                message.pprint(True)
                message.ack()

        except KeyboardInterrupt:
            print('Exited consumer')
