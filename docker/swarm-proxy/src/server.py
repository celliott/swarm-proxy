#!/usr/bin/python

import os
import json
import options
import logging
from flask import request, Response

server = flask.Flask(__name__)
options = options.get_options()
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

@server.route("/create_service", methods=['POST'])
def create_service():
  data = json.loads(request.data)
  try:
    results = options['docker'].services.create(
        image = data['name'],
        name = = data['name'],
        replicas = data['replicas'],
        restart-condition = "any",
        networks = data['network'],
        container_labels = data['network'],
        env = data['env'],
        port = data['port'],
    )
  except: pass
  return flask.jsonify({"results":results.replace('\n','')})

@server.route("/rm_service", methods=['DELETE'])
def rm_service():
  data = json.loads(request.data)
  try:
    results = options['docker'].services.remove(
        image = data['name'],
    )
  except: pass
  return flask.jsonify({"results":results.replace('\n','')})

if __name__ == "__main__":
  server.run(host='0.0.0.0', port=options['server_port'])
