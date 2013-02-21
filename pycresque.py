import redis, json

class Cresque:
    def __init__(self, host, port=6379):
        self.redis = redis.Redis(host, port)

    def enqueue(self, queue, name, args):
        queue_name = 'resque:queue:' + queue
        pay_load = json.dumps({ 'class' : name, 'args': args})
        self.redis.rpush(queue_name, pay_load)
