# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: futuracommon/protos/backend_change.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(futuracommon/protos/backend_change.proto\x12\x07\x62\x61\x63kend\"%\n\rBackendConfig\x12\x14\n\x0c\x62\x61\x63kend_name\x18\x01 \x01(\t\"1\n\rBackendStatus\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1f\n\x0b\x42\x61\x63kendList\x12\x10\n\x08\x62\x61\x63kends\x18\x01 \x03(\t\"\x07\n\x05\x45mpty2\x89\x01\n\x0e\x42\x61\x63kendService\x12?\n\rChangeBackend\x12\x16.backend.BackendConfig\x1a\x16.backend.BackendStatus\x12\x36\n\x0eGetBackendList\x12\x0e.backend.Empty\x1a\x14.backend.BackendListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'futuracommon.protos.backend_change_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BACKENDCONFIG']._serialized_start=53
  _globals['_BACKENDCONFIG']._serialized_end=90
  _globals['_BACKENDSTATUS']._serialized_start=92
  _globals['_BACKENDSTATUS']._serialized_end=141
  _globals['_BACKENDLIST']._serialized_start=143
  _globals['_BACKENDLIST']._serialized_end=174
  _globals['_EMPTY']._serialized_start=176
  _globals['_EMPTY']._serialized_end=183
  _globals['_BACKENDSERVICE']._serialized_start=186
  _globals['_BACKENDSERVICE']._serialized_end=323
# @@protoc_insertion_point(module_scope)
