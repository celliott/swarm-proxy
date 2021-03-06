#!/usr/bin/env python

import os
import json
import flask
import options
import logging
import subprocess
from flask import request, Response

server = flask.Flask(__name__)
options = options.get_options()
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

@server.route("/create_service", methods=['POST'])
def create_service():
    data = json.loads(request.data)
    try:
        cmd = "/usr/bin/docker service create --replicas 1 --restart-condition any --name {name} --network {network} --container-label {label} -e {env} -p {port} {image}".format(**data)
        results = subprocess.check_output(cmd, shell=True)
        return flask.jsonify({"results":results.replace('\n','')}), 201, {'ContentType':'application/json'}
    except:
        return flask.jsonify({"msg": "Error, Service Not Added"}), 500, {'ContentType':'application/json'}

@server.route("/rm_service", methods=['DELETE'])
def rm_service():
    data = json.loads(request.data)
    try:
        cmd = "/usr/bin/docker service rm {name}".format(**data)
        results = subprocess.check_output(cmd, shell=True)
        return flask.jsonify({"results":results.replace('\n','')}), 202, {'ContentType':'application/json'}
    except:
        return flask.jsonify({"msg": "Error, Service Not Removed"}), 500, {'ContentType':'application/json'}

if __name__ == "__main__":
  server.run(host='0.0.0.0', port=options['server_port'])
