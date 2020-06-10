

so sawtooth uses LMDB as a database, with a rust interface

[LMDB in source code](https://github.com/hyperledger/sawtooth-core/blob/master/validator/src/database/lmdb.rs)
[lmdb rust api](https://github.com/hyperledger/sawtooth-core/blob/master/validator/src/database/lmdb.rs)


The issue with the encryption being handled at the Interconnect level is that it might brake some unforseen logic specially when it comes to Sawtooth-seth. The proto for validator_pb2 messages would have to change. It's quite a huge drastic change to the project.

First of all the data structure would have to change
The global logic in the interconnect module would also have to change
The seth solidity smart contracts might have to change as well.
An additional reason why this approach would not work is that assuming that we forked and applied those changes on the interconnect module level. The problem would be that the validation of the messages happen on the Transaction processor anyways. So encrypted payload would be consider as an invalid when they happen to be Unpacked by either cbor or protobuf Grpc.

The most logical and easiest way to add encryption would be to write an external python module that would simply be called by TP's on their unpack method. This approach however has the effect of having to change the logic in transaction processors.

Advantage is that the cryptography is more limited in scope and more controlled. Since's it's not a global change to the codebase.
However it requires some code change from the developers writing those TP's. It seems that is is a logical thing to do thought, since developers are the ones would want to have cryptography on some transactions and not on some other TP's. A bit more complex on the usability side but that gives more technical control for the developer.












