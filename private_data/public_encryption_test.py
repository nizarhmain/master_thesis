
from ecies.utils import generate_key

from ecies import encrypt, decrypt

import binascii

import coincurve


pub = '0227ffac7d33231086df84e12f0856c0e985c18d3daa2c94c7abcbff9a6aa8b258'
priv = 'ee113297d1fb3c214722aadf59a3d94dff24264ffc5c34b78c903b36eb1aeca8'

# print(pub)

coincurve_privk = coincurve.PrivateKey.from_hex(priv)

print(coincurve_privk.secret)

k = generate_key()

# print(dir(k))

# print(bytes(str(k), 'utf-8').hex())

sk_hex = coincurve_privk.secret
pk_hex = coincurve_privk.public_key.format(True)

# print(k.secret)

print(decrypt(sk_hex, encrypt(pk_hex, b'this is data')))

# print(sk_hex.hex())
# print(pk_hex.hex())



# print(pubhex)








