from flask import Flask, abort

import socket
import time

app = Flask(__name__)

hostname = socket.gethostname()


@app.route('/')
def hello():
    return "hello from v2 on host {}\n".format(hostname)


@app.route('/live')
def live():
    return "OK"


@app.route('/ready')
def ready():
    return "Yes"


if __name__ == '__main__':
    time.sleep(3)
    app.run(host='0.0.0.0', port=8080)
    time.sleep(1)
