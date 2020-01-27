from flask import Flask, abort

import socket
import time

import signal
import sys

def sigterm_handler(_signo, _stack_frame):
    print("Exiting exam")
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

app = Flask(__name__)

hostname = socket.gethostname()


@app.route('/')
def hello():
    return "hello from v3 on host {}\n".format(hostname)


@app.route('/live')
def live():
    return "OK"


@app.route('/ready')
def ready():
    return "Yes"


if __name__ == '__main__':
    time.sleep(3)
    app.run(host='0.0.0.0', port=8080)
    print("Exiting exam")
    time.sleep(1)
