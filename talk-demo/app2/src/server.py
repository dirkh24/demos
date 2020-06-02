import os
import flask
import json
import ptvsd
#ptvsd.enable_attach(address=('0.0.0.0', 5678))

server = flask.Flask(__name__)
conn = None

@server.route('/')
def hello():
    return flask.jsonify({"response": "Hello from App2!!"})


if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=6000)
    # to use the ptvsd debugger we have to disable debug mode in flask
    #server.run(host='0.0.0.0', port=6000)
