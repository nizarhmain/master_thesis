
# should be very similar to the xo_client
# read the transaction family description and docs and then map that into code.
# the sawtooth_sdk protobuf libraries make that simple

from urllib.error import HTTPError
import urllib.request
from sawtooth_sdk.protobuf.batch_pb2 import BatchList
from sawtooth_sdk.protobuf.batch_pb2 import Batch

import cbor

import protosma_pb2

from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory

import hashlib

from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader
from sawtooth_sdk.protobuf.transaction_pb2 import Transaction


from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader

# print(dir(protosma_pb2.SmallbankTransactionPayload))


context = create_context('secp256k1')
private_key = context.new_random_private_key()
signer = CryptoFactory(context).new_signer(private_key)


def _sha512_small_bank(customer_id):
    return hashlib.sha512('smallbank'.encode('utf-8')).hexdigest()[0:6] + hashlib.sha512(str(customer_id).encode('utf-8')).hexdigest()[-64:]


customer1 = _sha512_small_bank(1)

print(customer1)

# create account for customer 1

'''
message CreateAccountTransactionData {
        // The CreateAccountTransaction creates an account

        // Customer ID
        uint32 customer_id = 1;

        // Customer Name
        string customer_name = 2;

        // Initial Savings Balance (in cents to avoid float)
        uint32 initial_savings_balance = 3;

        // Initial Checking Balance (in cents to avoid float)
        uint32 initial_checking_balance = 4;
    }
'''

# creating new accounts
small_payload = protosma_pb2.SmallbankTransactionPayload(
    payload_type=protosma_pb2.SmallbankTransactionPayload.CREATE_ACCOUNT,
    create_account=protosma_pb2.SmallbankTransactionPayload.CreateAccountTransactionData(
        customer_id=1,
        customer_name='eric',
        initial_savings_balance=2000,
        initial_checking_balance=1500
    )
)

payload_bytes = small_payload.SerializeToString()

print(small_payload)
print(payload_bytes)

# print(payload_bytes)

# create transaction headers

# addresses


print([customer1])

txn_header_bytes = TransactionHeader(
    family_name='smallbank',
    family_version='1.0',
    inputs=[customer1],
    outputs=[customer1],
    signer_public_key=signer.get_public_key().as_hex(),
    # In this example, we're signing the batch with the same private key,
    # but the batch can be signed by another party, in which case, the
    # public key will need to be associated with that key.
    batcher_public_key=signer.get_public_key().as_hex(),
    # In this example, there are no dependencies.  This list should include
    # an previous transaction header signatures that must be applied for
    # this transaction to successfully commit.
    # For example,
    # dependencies=['540a6803971d1880ec73a96cb97815a95d374cbad5d865925e5aa0432fcf1931539afe10310c122c5eaae15df61236079abbf4f258889359c4d175516934484a'],
    dependencies=[customer1],
    payload_sha512=hashlib.sha512(payload_bytes).hexdigest()
).SerializeToString()


# print(txn_header_bytes)

signature = signer.sign(txn_header_bytes)

# two mistakes synthactical mistakes !! on the wiki
txn = Transaction(header=txn_header_bytes,
                  header_signature=signature, payload=payload_bytes)


txns = [txn]

batch_header_bytes = BatchHeader(
    signer_public_key=signer.get_public_key().as_hex(),
    transaction_ids=[txn.header_signature for txn in txns],
).SerializeToString()


# print(signature)


signature = signer.sign(batch_header_bytes)

batch = Batch(
    header=batch_header_bytes,
    header_signature=signature,
    transactions=txns
)

batch_list_bytes = BatchList(batches=[batch]).SerializeToString()


# print(batch_list_bytes)


# send the batches


try:
    request = urllib.request.Request(
        'http://localhost:8008/batches',
        batch_list_bytes,
        method='POST',
        headers={'Content-Type': 'application/octet-stream'})
    response = urllib.request.urlopen(request)
    print(response.status)

except HTTPError as e:
    response = e.file

