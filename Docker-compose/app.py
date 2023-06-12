from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis()

@app.route('/')
def hello():
    # Increase the visit count stored in Redis
    redis.incr('visit_count')

    # Get the updated visit count from Redis
    visit_count = redis.get('visit_count').decode('utf-8')

    return f'Hello, world! You have visited this site {visit_count} times.'

if __name__ == '__main__':
    app.run()
