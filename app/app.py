from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis database
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = os.getenv('REDIS_PORT', 6379)
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def index():
    try:
        # Increment counter in Redis
        counter = redis_client.incr('counter')
        return f'Counter: {counter}'
    except redis.exceptions.ConnectionError:
        return 'Could not connect to Redis', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

