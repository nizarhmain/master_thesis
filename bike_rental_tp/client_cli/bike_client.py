import hashlib
import base64
import time
import random
import requests
import yaml
import cbor

from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory
from sawtooth_signing import ParseError
from sawtooth_signing.secp256k1 import Secp256k1PrivateKey

from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader
from sawtooth_sdk.protobuf.transaction_pb2 import Transaction
from sawtooth_sdk.protobuf.batch_pb2 import BatchList
from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader
from sawtooth_sdk.protobuf.batch_pb2 import Batch


def _sha512(data):
    return hashlib.sha512(data).hexdigest()


class BikeClient:
    def __init__(self, url, keyfile=None):
        self.url = url

        # signing part

        context = create_context('secp256k1')
        private_key = context.new_random_private_key()

        # sets the signer with the random private key signing
        print(private_key)
        self._signer = CryptoFactory(context).new_signer(private_key)

    def create_bike(self, payload, wait=None):
        return self._send_transaction('create_bike_tx', payload, wait=wait)

    def set(self, name, value, wait=None):
        return self._send_transaction('set', name, value, wait=wait)

    def inc(self, name, value, wait=None):
        return self._send_transaction('inc', name, value, wait=wait)

    def dec(self, name, value, wait=None):
        return self._send_transaction('dec', name, value, wait=wait)

    def list(self):
        result = self._send_request(
            "state?address={}".format(
                self._get_prefix()))

        try:
            encoded_entries = yaml.safe_load(result)["data"]

            return [
                cbor.loads(base64.b64decode(entry["data"]))
                for entry in encoded_entries
            ]

        except BaseException:
            return None

    def show(self, name):
        address = self._get_address(name)

        result = self._send_request("state/{}".format(address), name=name,)

        try:
            return cbor.loads(
                base64.b64decode(
                    yaml.safe_load(result)["data"]))[name]

        except BaseException:
            return None

    def _get_status(self, batch_id, wait):
        try:
            result = self._send_request(
                'batch_statuses?id={}&wait={}'.format(batch_id, wait),)
            return yaml.safe_load(result)['data'][0]['status']
        except BaseException as err:
            raise BikeClientException(err)

    def _get_prefix(self):
        return _sha512('bike'.encode('utf-8'))[0:6]

    def _get_address(self, bikeType):
        prefix = self._get_prefix()
        bike_storage = _sha512(bikeType.encode('utf-8'))[64:]
        return prefix + bike_storage

    def _send_request(self, suffix, data=None, content_type=None, name=None):
        if self.url.startswith("http://"):
            url = "{}/{}".format(self.url, suffix)
        else:
            url = "http://{}/{}".format(self.url, suffix)

        headers = {}

        if content_type is not None:
            headers['Content-Type'] = content_type

        try:
            if data is not None:
                result = requests.post(url, headers=headers, data=data)
            else:
                result = requests.get(url, headers=headers)

            if result.status_code == 404:
                raise BikeClientException("No such key: {}".format(name))

            if not result.ok:
                raise BikeClientException("Error {}: {}".format(
                    result.status_code, result.reason))

        except requests.ConnectionError as err:
            raise BikeClientException(
                'Failed to connect to REST API: {}'.format(err))

        except BaseException as err:
            raise BikeClientException(err)

        return result.text

    # the payload is already the cbor dump
    def _send_transaction(self, type, payload, wait=None):

        bikeType_addr = cbor.loads(payload)['bikeType']

        # Construct the address
        address = self._get_address(bikeType_addr)

        print(address)

        header = TransactionHeader(
            signer_public_key=self._signer.get_public_key().as_hex(),
            family_name="bike",
            family_version="1.0",
            inputs=[address],
            outputs=[address],
            dependencies=[],
            payload_sha512=_sha512(payload),
            batcher_public_key=self._signer.get_public_key().as_hex(),
            nonce=hex(random.randint(0, 2**64))
        ).SerializeToString()

        signature = self._signer.sign(header)

        transaction = Transaction(
            header=header,
            payload=payload,
            header_signature=signature
        )

        batch_list = self._create_batch_list([transaction])
        batch_id = batch_list.batches[0].header_signature

        if wait and wait > 0:
            wait_time = 0
            start_time = time.time()
            response = self._send_request(
                "batches", batch_list.SerializeToString(),
                'application/octet-stream',
            )
            while wait_time < wait:
                status = self._get_status(
                    batch_id,
                    wait - int(wait_time),
                )
                wait_time = time.time() - start_time

                if status != 'PENDING':
                    return response

            return response

        return self._send_request(
            "batches", batch_list.SerializeToString(),
            'application/octet-stream',
        )

    def _create_batch_list(self, transactions):
        transaction_signatures = [t.header_signature for t in transactions]

        header = BatchHeader(
            signer_public_key=self._signer.get_public_key().as_hex(),
            transaction_ids=transaction_signatures
        ).SerializeToString()

        signature = self._signer.sign(header)

        batch = Batch(
            header=header,
            transactions=transactions,
            header_signature=signature)
        return BatchList(batches=[batch])


bk = BikeClient('http://localhost:8008')

first_create_payload = cbor.dumps({
    'Type': 'create_bike_tx',
    'bikeType': 'racing bike',
    'available': 9
})

bk.create_bike(first_create_payload)

