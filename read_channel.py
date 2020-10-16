#!/usr/bin/env python3

import yaml

def generate_channel():
    with open('channel.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return(data)
