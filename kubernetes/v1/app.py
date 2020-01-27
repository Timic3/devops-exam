from flask import Flask

import socket
import time

app = Flask(__name__)

hostname = socket.gethostname()


@app.route('/')
def hello():
    return "hello from v1 on {}\n".format(hostname)


if __name__ == '__main__':
    time.sleep(3)
    app.run(host='0.0.0.0', port=8080)
    time.sleep(1)