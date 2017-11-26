#!/usr/bin/env python

import os
import docker

def get_options():
    return {
        'server_name': os.getenv('SWARM_PROXY_SERVICE_NAME', 'swarm01'),
        'server_port': os.getenv('SWARM_PROXY_PORT', '3000'),
        'docker': docker.Client(base_url='unix://var/run/docker.sock'),
    }
