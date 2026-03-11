#!/usr/bin/env python3

import yaml
import os
import glob

PATH = 'items/'  # Directory where I can find the podcast chapters


def generate_items():
    '''
    This function returns a list of dictionaries generated from the yaml files in
    the directory defined in PATH
    '''
    items = []
    for filename in glob.glob(os.path.join(PATH, '*.yaml')):
        with open(filename, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            items.append(data)
    return items
