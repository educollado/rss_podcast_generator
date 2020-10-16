#!/usr/bin/env python3

import yaml
import os
import glob
path='items/'
items=[]
def generate_items():
    for filename in glob.glob(os.path.join(path, '*.yaml')):
        with open(os.path.join(filename), 'r') as f: # open in readonly mode
            data = yaml.load(f, Loader=yaml.FullLoader)
            items.append(data)
    return(items)
