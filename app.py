from flask import Flask
import redis
import os
import socket

# Connect to Redis
pool = redis.ConnectionPool(host='192.168.1.103', port=6379, db=0)
Redis = redis.Redis(connection_pool=pool)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        print "Trying to connect"
        visits = Redis.incr("counter")
        print "should work"
    except redis.RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
