# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: futuracommon/protos/nlp.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x66uturacommon/protos/nlp.proto\x12\x03nlp\";\n\x13SuccessNotification\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\",\n\x14NotificationResponse\x12\x14\n\x0c\x61\x63knowledged\x18\x01 \x01(\x08\x32R\n\nNLPService\x12\x44\n\rNotifySuccess\x12\x18.nlp.SuccessNotification\x1a\x19.nlp.NotificationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'futuracommon.protos.nlp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SUCCESSNOTIFICATION']._serialized_start=38
  _globals['_SUCCESSNOTIFICATION']._serialized_end=97
  _globals['_NOTIFICATIONRESPONSE']._serialized_start=99
  _globals['_NOTIFICATIONRESPONSE']._serialized_end=143
  _globals['_NLPSERVICE']._serialized_start=145
  _globals['_NLPSERVICE']._serialized_end=227
# @@protoc_insertion_point(module_scope)
