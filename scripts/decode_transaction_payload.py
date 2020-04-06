import base64

import cbor

payload = {
    'Verb': 'set',
    'Name': 'foo',
    'Value': 42}

payload_bytes = cbor.dumps(payload)


# using cbor we can get the python object from the binary

settings64 = 'CAESgAEKJnNhd3Rvb3RoLnNldHRpbmdzLnZvdGUuYXV0aG9yaXplZF9rZXlzEkIwMjA3MmM2NjljZDU1MjE1Yjk5OTc1OTExZTI2MDhlMGQ2ODJiZGJjOWI0ZTgwNjhhZTgzYjA4ZDk1MmNmNDc5OGUaEjB4NTgzNWY0Yjg2ZTc2ZGE0Nw=='

decoded_settings = base64.b64decode(settings64)

print(decoded_settings)

loaded_data = cbor.loads(b'\xa1frMKhhA\x19\xba\x88')
# loaded_data = cbor.loads(b'\xa1frMKhhA\x19\xba\x88')
# loaded_data = cbor.loads(b'\nl\n&sawtooth.settings.vote.authorized_keys\x12B032cc920a88536a2e4a011f8aa1bbd65f1dd6136cf252539817bf6af9104835239')


# loaded_data = cbor.loads(b'\n+\n$sawtooth.consensus.algorithm.version\x12\x030.1')


# loaded_data = cbor.loads(b'\n,\n!sawtooth.consensus.algorithm.name\x12\x07Devmode')

# print(payload_bytes)

print(loaded_data)

