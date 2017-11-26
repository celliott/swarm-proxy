#!/usr/bin/env python

import os

def get_options():
    return {
        'server_name': os.getenv('SWARM_PROXY_SERVICE_NAME', 'swarm01'),
        'server_port': os.getenv('SWARM_PROXY_PORT', '4000'),
    }
