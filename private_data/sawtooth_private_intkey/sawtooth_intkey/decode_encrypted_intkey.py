import base64

import cbor

import os


import sys

from sawtooth_intkey.enclave import enclave_dec 

PRIVATE_KEY = ''

with open('private_key', 'r') as file:
    data = file.read().replace('\n', '')
    # print(data)
    PRIVATE_KEY = data

# read from private key file

# x = base64.b64decode('o2RWZXJiY3NldGROYW1lZnNlY29uZGVWYWx1ZVhjBBg33ckRwVHooczrLUE7nQGipwfHqUhU8TRGqet2vs96fJiLjvnbS/HEU6jOz438/q+XPYqafaC7cYoqsurxXtGtGjxmCVC/nm7nwOBn926sQ8KIdi5ifrbRAiy2V0BVw4tf')

print(sys.argv[1])

x = base64.b64decode(sys.argv[1])

loaded_cbor = cbor.loads(x)

print(loaded_cbor)

decrypted = enclave_dec(PRIVATE_KEY, loaded_cbor['Value'])

print(int.from_bytes(decrypted, 'big'))

# print(str(x['Value']))














