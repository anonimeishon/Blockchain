from hashlib import sha256
import json
import time
import sys
import argparse


def compute_hash():
    #filename = sys.argv[-1]
    print(sys.argv[-1])
    #block_string = json.dumps({'student': 'dildo perez'}, sort_keys=True)
    block_string = json.dumps(sys.argv[-1])
    return sha256(block_string.encode()).hexdigest()


print(compute_hash())
