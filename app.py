from flask import Flask
import socket

container_hostname = socket.gethostname()
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

app.run(host='0.0.0.0')