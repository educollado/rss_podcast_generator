#!/usr/bin/env python3

import yaml
import os
import glob
path='items/' # Directory where I can find the podcast chapters
items=[] # empty list of dictonaries
def generate_items():
    '''
    This function returns a list of dictionaries generated from the yaml files int
    the directory defined in path
    '''
    for filename in glob.glob(os.path.join(path, '*.yaml')):
        with open(os.path.join(filename), 'r') as f: # open in readonly mode
            data = yaml.load(f, Loader=yaml.FullLoader)
            items.append(data)
    return(items)
