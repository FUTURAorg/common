# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: futuracommon/protos/imageservice.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&futuracommon/protos/imageservice.proto\x12\x0biamgestream\"4\n\tImageData\x12\x14\n\x0cimage_base64\x18\x01 \x01(\x0c\x12\x11\n\tclient_id\x18\x02 \x01(\t\".\n\rStreamSummary\x12\x1d\n\x15total_images_received\x18\x01 \x01(\x05\x32Z\n\x12ImageStreamService\x12\x44\n\nSendImages\x12\x16.iamgestream.ImageData\x1a\x1a.iamgestream.StreamSummary\"\x00(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'futuracommon.protos.imageservice_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_IMAGEDATA']._serialized_start=55
  _globals['_IMAGEDATA']._serialized_end=107
  _globals['_STREAMSUMMARY']._serialized_start=109
  _globals['_STREAMSUMMARY']._serialized_end=155
  _globals['_IMAGESTREAMSERVICE']._serialized_start=157
  _globals['_IMAGESTREAMSERVICE']._serialized_end=247
# @@protoc_insertion_point(module_scope)
