#!/usr/bin/env python3

import yaml

def generate_channel():
    '''
    This function returns a dictionary generated from the yaml file
    '''
    with open('channel.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return(data)
