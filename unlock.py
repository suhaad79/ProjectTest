#!/usr/bin/env python3

import os
import argparse
from base64 import b64decode

parser = argparse.ArgumentParser(description='Decrypts repository')

parser.add_argument(
    'key', type=str, help='Base64-encoded key to unlock repository')
parser.add_argument('--path', type=argparse.FileType('wb'),
                    default='../git-crypt-key', help="Path to the git-crypt key file (default: '../git-crypt-key')")

args = parser.parse_args()

key = b64decode(args.key)
args.path.write(key)
args.path.close()

os.system(f"git-crypt unlock {args.path.name}")
