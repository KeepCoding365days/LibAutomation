
import redis
import json
from django.conf import settings

# Initialize Redis client
redis_client = redis.StrictRedis.from_url(settings.CACHES['default']['LOCATION'])

def append_to_queue(data):
    redis_client.lpush('data_queue', data)


def get_first_from_queue():

    item = redis_client.rpop('data_queue')  # Get the first element (rightmost)

    if item:
        return item
    return None

class queue:
    q=[]
    def __init__(self):
        self.q=[]
    def append(self,data):
        self.q.append(data)
    def pop(self):
        if len(self.q)>0:
            first=self.q[0]
            self.q=self.q.pop(0)
            return first
        else:
            return None

book_que=queue()