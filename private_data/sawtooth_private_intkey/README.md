# start the TP

./start_tp

# set a value in the key value ledger

python3 -m sawtooth_intkey.client_cli.intkey_cli set fourth 14 --keyfile private_key

# decodes the encrypted value on the ledger based on the privateFor elements, for now its a simple key, but we can ofc extend that to a list

python3 -m sawtooth_intkey.decode_encrypted_intkey pGRWZXJiY3NldGROYW1lZXRoaXJkZVZhbHVlWGMEhUsB4AACU6AJ7vsDXinftdcG7MVSdqQqhf/XnceZ6kUen1rRxa74dkkh7H8TBksBohp4JFv8kjpnx3thsP1JX4M1ZiVt46wEpqTLd04PfN+z1pq8tTSpevqZLkFmhElTAClrUHJpdmF0ZV9Gb3J4QjAyMjdmZmFjN2QzMzIzMTA4NmRmODRlMTJmMDg1NmMwZTk4NWMxOGQzZGFhMmM5NGM3YWJjYmZmOWE2YWE4YjI1OA==




