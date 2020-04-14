# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smallbank.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='smallbank.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('Z\rsmallbank_pb2'),
  serialized_pb=_b('\n\x0fsmallbank.proto\"h\n\x07\x41\x63\x63ount\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\r\x12\x15\n\rcustomer_name\x18\x02 \x01(\t\x12\x17\n\x0fsavings_balance\x18\x03 \x01(\r\x12\x18\n\x10\x63hecking_balance\x18\x04 \x01(\r\"\xf8\t\n\x1bSmallbankTransactionPayload\x12>\n\x0cpayload_type\x18\x01 \x01(\x0e\x32(.SmallbankTransactionPayload.PayloadType\x12Q\n\x0e\x63reate_account\x18\x02 \x01(\x0b\x32\x39.SmallbankTransactionPayload.CreateAccountTransactionData\x12U\n\x10\x64\x65posit_checking\x18\x03 \x01(\x0b\x32;.SmallbankTransactionPayload.DepositCheckingTransactionData\x12K\n\x0bwrite_check\x18\x04 \x01(\x0b\x32\x36.SmallbankTransactionPayload.WriteCheckTransactionData\x12U\n\x10transact_savings\x18\x05 \x01(\x0b\x32;.SmallbankTransactionPayload.TransactSavingsTransactionData\x12M\n\x0csend_payment\x18\x06 \x01(\x0b\x32\x37.SmallbankTransactionPayload.SendPaymentTransactionData\x12J\n\namalgamate\x18\x07 \x01(\x0b\x32\x36.SmallbankTransactionPayload.AmalgamateTransactionData\x1a\x8d\x01\n\x1c\x43reateAccountTransactionData\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\r\x12\x15\n\rcustomer_name\x18\x02 \x01(\t\x12\x1f\n\x17initial_savings_balance\x18\x03 \x01(\r\x12 \n\x18initial_checking_balance\x18\x04 \x01(\r\x1a\x45\n\x1e\x44\x65positCheckingTransactionData\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61mount\x18\x02 \x01(\r\x1a@\n\x19WriteCheckTransactionData\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61mount\x18\x02 \x01(\r\x1a\x45\n\x1eTransactSavingsTransactionData\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\x1a\x62\n\x1aSendPaymentTransactionData\x12\x1a\n\x12source_customer_id\x18\x01 \x01(\r\x12\x18\n\x10\x64\x65st_customer_id\x18\x02 \x01(\r\x12\x0e\n\x06\x61mount\x18\x03 \x01(\r\x1aQ\n\x19\x41malgamateTransactionData\x12\x1a\n\x12source_customer_id\x18\x01 \x01(\r\x12\x18\n\x10\x64\x65st_customer_id\x18\x02 \x01(\r\"\x98\x01\n\x0bPayloadType\x12\x16\n\x12PAYLOAD_TYPE_UNSET\x10\x00\x12\x12\n\x0e\x43REATE_ACCOUNT\x10\x01\x12\x14\n\x10\x44\x45POSIT_CHECKING\x10\x02\x12\x0f\n\x0bWRITE_CHECK\x10\x03\x12\x14\n\x10TRANSACT_SAVINGS\x10\x04\x12\x10\n\x0cSEND_PAYMENT\x10\x05\x12\x0e\n\nAMALGAMATE\x10\x06\x42\x0fZ\rsmallbank_pb2b\x06proto3')
)



_SMALLBANKTRANSACTIONPAYLOAD_PAYLOADTYPE = _descriptor.EnumDescriptor(
  name='PayloadType',
  full_name='SmallbankTransactionPayload.PayloadType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PAYLOAD_TYPE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_ACCOUNT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPOSIT_CHECKING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE_CHECK', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSACT_SAVINGS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_PAYMENT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AMALGAMATE', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1246,
  serialized_end=1398,
)
_sym_db.RegisterEnumDescriptor(_SMALLBANKTRANSACTIONPAYLOAD_PAYLOADTYPE)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='Account.customer_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer_name', full_name='Account.customer_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='savings_balance', full_name='Account.savings_balance', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checking_balance', full_name='Account.checking_balance', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=123,
)


_SMALLBANKTRANSACTIONPAYLOAD_CREATEACCOUNTTRANSACTIONDATA = _descriptor.Descriptor(
  name='CreateAccountTransactionData',
  full_name='SmallbankTransactionPayload.CreateAccountTransactionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='SmallbankTransactionPayload.CreateAccountTransactionData.customer_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer_name', full_name='SmallbankTransactionPayload.CreateAccountTransactionData.customer_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_savings_balance', full_name='SmallbankTransactionPayload.CreateAccountTransactionData.initial_savings_balance', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_checking_balance', full_name='SmallbankTransactionPayload.CreateAccountTransactionData.initial_checking_balance', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=711,
  serialized_end=852,
)

_SMALLBANKTRANSACTIONPAYLOAD_DEPOSITCHECKINGTRANSACTIONDATA = _descriptor.Descriptor(
  name='DepositCheckingTransactionData',
  full_name='SmallbankTransactionPayload.DepositCheckingTransactionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='SmallbankTransactionPayload.DepositCheckingTransactionData.customer_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='SmallbankTransactionPayload.DepositCheckingTransactionData.amount', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=854,
  serialized_end=923,
)

_SMALLBANKTRANSACTIONPAYLOAD_WRITECHECKTRANSACTIONDATA = _descriptor.Descriptor(
  name='WriteCheckTransactionData',
  full_name='SmallbankTransactionPayload.WriteCheckTransactionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='SmallbankTransactionPayload.WriteCheckTransactionData.customer_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='SmallbankTransactionPayload.WriteCheckTransactionData.amount', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=925,
  serialized_end=989,
)

_SMALLBANKTRANSACTIONPAYLOAD_TRANSACTSAVINGSTRANSACTIONDATA = _descriptor.Descriptor(
  name='TransactSavingsTransactionData',
  full_name='SmallbankTransactionPayload.TransactSavingsTransactionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='SmallbankTransactionPayload.TransactSavingsTransactionData.customer_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='SmallbankTransactionPayload.TransactSavingsTransactionData.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=991,
  serialized_end=1060,
)

_SMALLBANKTRANSACTIONPAYLOAD_SENDPAYMENTTRANSACTIONDATA = _descriptor.Descriptor(
  name='SendPaymentTransactionData',
  full_name='SmallbankTransactionPayload.SendPaymentTransactionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_customer_id', full_name='SmallbankTransactionPayload.SendPaymentTransactionData.source_customer_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_customer_id', full_name='SmallbankTransactionPayload.SendPaymentTransactionData.dest_customer_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='SmallbankTransactionPayload.SendPaymentTransactionData.amount', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1062,
  serialized_end=1160,
)

_SMALLBANKTRANSACTIONPAYLOAD_AMALGAMATETRANSACTIONDATA = _descriptor.Descriptor(
  name='AmalgamateTransactionData',
  full_name='SmallbankTransactionPayload.AmalgamateTransactionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_customer_id', full_name='SmallbankTransactionPayload.AmalgamateTransactionData.source_customer_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_customer_id', full_name='SmallbankTransactionPayload.AmalgamateTransactionData.dest_customer_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1162,
  serialized_end=1243,
)

_SMALLBANKTRANSACTIONPAYLOAD = _descriptor.Descriptor(
  name='SmallbankTransactionPayload',
  full_name='SmallbankTransactionPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload_type', full_name='SmallbankTransactionPayload.payload_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_account', full_name='SmallbankTransactionPayload.create_account', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deposit_checking', full_name='SmallbankTransactionPayload.deposit_checking', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='write_check', full_name='SmallbankTransactionPayload.write_check', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transact_savings', full_name='SmallbankTransactionPayload.transact_savings', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send_payment', full_name='SmallbankTransactionPayload.send_payment', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amalgamate', full_name='SmallbankTransactionPayload.amalgamate', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SMALLBANKTRANSACTIONPAYLOAD_CREATEACCOUNTTRANSACTIONDATA, _SMALLBANKTRANSACTIONPAYLOAD_DEPOSITCHECKINGTRANSACTIONDATA, _SMALLBANKTRANSACTIONPAYLOAD_WRITECHECKTRANSACTIONDATA, _SMALLBANKTRANSACTIONPAYLOAD_TRANSACTSAVINGSTRANSACTIONDATA, _SMALLBANKTRANSACTIONPAYLOAD_SENDPAYMENTTRANSACTIONDATA, _SMALLBANKTRANSACTIONPAYLOAD_AMALGAMATETRANSACTIONDATA, ],
  enum_types=[
    _SMALLBANKTRANSACTIONPAYLOAD_PAYLOADTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=1398,
)

_SMALLBANKTRANSACTIONPAYLOAD_CREATEACCOUNTTRANSACTIONDATA.containing_type = _SMALLBANKTRANSACTIONPAYLOAD
_SMALLBANKTRANSACTIONPAYLOAD_DEPOSITCHECKINGTRANSACTIONDATA.containing_type = _SMALLBANKTRANSACTIONPAYLOAD
_SMALLBANKTRANSACTIONPAYLOAD_WRITECHECKTRANSACTIONDATA.containing_type = _SMALLBANKTRANSACTIONPAYLOAD
_SMALLBANKTRANSACTIONPAYLOAD_TRANSACTSAVINGSTRANSACTIONDATA.containing_type = _SMALLBANKTRANSACTIONPAYLOAD
_SMALLBANKTRANSACTIONPAYLOAD_SENDPAYMENTTRANSACTIONDATA.containing_type = _SMALLBANKTRANSACTIONPAYLOAD
_SMALLBANKTRANSACTIONPAYLOAD_AMALGAMATETRANSACTIONDATA.containing_type = _SMALLBANKTRANSACTIONPAYLOAD
_SMALLBANKTRANSACTIONPAYLOAD.fields_by_name['payload_type'].enum_type = _SMALLBANKTRANSACTIONPAYLOAD_PAYLOADTYPE
_SMALLBANKTRANSACTIONPAYLOAD.fields_by_name['create_account'].message_type = _SMALLBANKTRANSACTIONPAYLOAD_CREATEACCOUNTTRANSACTIONDATA
_SMALLBANKTRANSACTIONPAYLOAD.fields_by_name['deposit_checking'].message_type = _SMALLBANKTRANSACTIONPAYLOAD_DEPOSITCHECKINGTRANSACTIONDATA
_SMALLBANKTRANSACTIONPAYLOAD.fields_by_name['write_check'].message_type = _SMALLBANKTRANSACTIONPAYLOAD_WRITECHECKTRANSACTIONDATA
_SMALLBANKTRANSACTIONPAYLOAD.fields_by_name['transact_savings'].message_type = _SMALLBANKTRANSACTIONPAYLOAD_TRANSACTSAVINGSTRANSACTIONDATA
_SMALLBANKTRANSACTIONPAYLOAD.fields_by_name['send_payment'].message_type = _SMALLBANKTRANSACTIONPAYLOAD_SENDPAYMENTTRANSACTIONDATA
_SMALLBANKTRANSACTIONPAYLOAD.fields_by_name['amalgamate'].message_type = _SMALLBANKTRANSACTIONPAYLOAD_AMALGAMATETRANSACTIONDATA
_SMALLBANKTRANSACTIONPAYLOAD_PAYLOADTYPE.containing_type = _SMALLBANKTRANSACTIONPAYLOAD
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['SmallbankTransactionPayload'] = _SMALLBANKTRANSACTIONPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT,
  __module__ = 'smallbank_pb2'
  # @@protoc_insertion_point(class_scope:Account)
  ))
_sym_db.RegisterMessage(Account)

SmallbankTransactionPayload = _reflection.GeneratedProtocolMessageType('SmallbankTransactionPayload', (_message.Message,), dict(

  CreateAccountTransactionData = _reflection.GeneratedProtocolMessageType('CreateAccountTransactionData', (_message.Message,), dict(
    DESCRIPTOR = _SMALLBANKTRANSACTIONPAYLOAD_CREATEACCOUNTTRANSACTIONDATA,
    __module__ = 'smallbank_pb2'
    # @@protoc_insertion_point(class_scope:SmallbankTransactionPayload.CreateAccountTransactionData)
    ))
  ,

  DepositCheckingTransactionData = _reflection.GeneratedProtocolMessageType('DepositCheckingTransactionData', (_message.Message,), dict(
    DESCRIPTOR = _SMALLBANKTRANSACTIONPAYLOAD_DEPOSITCHECKINGTRANSACTIONDATA,
    __module__ = 'smallbank_pb2'
    # @@protoc_insertion_point(class_scope:SmallbankTransactionPayload.DepositCheckingTransactionData)
    ))
  ,

  WriteCheckTransactionData = _reflection.GeneratedProtocolMessageType('WriteCheckTransactionData', (_message.Message,), dict(
    DESCRIPTOR = _SMALLBANKTRANSACTIONPAYLOAD_WRITECHECKTRANSACTIONDATA,
    __module__ = 'smallbank_pb2'
    # @@protoc_insertion_point(class_scope:SmallbankTransactionPayload.WriteCheckTransactionData)
    ))
  ,

  TransactSavingsTransactionData = _reflection.GeneratedProtocolMessageType('TransactSavingsTransactionData', (_message.Message,), dict(
    DESCRIPTOR = _SMALLBANKTRANSACTIONPAYLOAD_TRANSACTSAVINGSTRANSACTIONDATA,
    __module__ = 'smallbank_pb2'
    # @@protoc_insertion_point(class_scope:SmallbankTransactionPayload.TransactSavingsTransactionData)
    ))
  ,

  SendPaymentTransactionData = _reflection.GeneratedProtocolMessageType('SendPaymentTransactionData', (_message.Message,), dict(
    DESCRIPTOR = _SMALLBANKTRANSACTIONPAYLOAD_SENDPAYMENTTRANSACTIONDATA,
    __module__ = 'smallbank_pb2'
    # @@protoc_insertion_point(class_scope:SmallbankTransactionPayload.SendPaymentTransactionData)
    ))
  ,

  AmalgamateTransactionData = _reflection.GeneratedProtocolMessageType('AmalgamateTransactionData', (_message.Message,), dict(
    DESCRIPTOR = _SMALLBANKTRANSACTIONPAYLOAD_AMALGAMATETRANSACTIONDATA,
    __module__ = 'smallbank_pb2'
    # @@protoc_insertion_point(class_scope:SmallbankTransactionPayload.AmalgamateTransactionData)
    ))
  ,
  DESCRIPTOR = _SMALLBANKTRANSACTIONPAYLOAD,
  __module__ = 'smallbank_pb2'
  # @@protoc_insertion_point(class_scope:SmallbankTransactionPayload)
  ))
_sym_db.RegisterMessage(SmallbankTransactionPayload)
_sym_db.RegisterMessage(SmallbankTransactionPayload.CreateAccountTransactionData)
_sym_db.RegisterMessage(SmallbankTransactionPayload.DepositCheckingTransactionData)
_sym_db.RegisterMessage(SmallbankTransactionPayload.WriteCheckTransactionData)
_sym_db.RegisterMessage(SmallbankTransactionPayload.TransactSavingsTransactionData)
_sym_db.RegisterMessage(SmallbankTransactionPayload.SendPaymentTransactionData)
_sym_db.RegisterMessage(SmallbankTransactionPayload.AmalgamateTransactionData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)