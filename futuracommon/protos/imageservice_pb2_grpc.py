# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from futuracommon.protos import imageservice_pb2 as futuracommon_dot_protos_dot_imageservice__pb2


class ImageStreamServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendImages = channel.stream_unary(
                '/iamgestream.ImageStreamService/SendImages',
                request_serializer=futuracommon_dot_protos_dot_imageservice__pb2.ImageData.SerializeToString,
                response_deserializer=futuracommon_dot_protos_dot_imageservice__pb2.StreamSummary.FromString,
                )


class ImageStreamServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendImages(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageStreamServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendImages': grpc.stream_unary_rpc_method_handler(
                    servicer.SendImages,
                    request_deserializer=futuracommon_dot_protos_dot_imageservice__pb2.ImageData.FromString,
                    response_serializer=futuracommon_dot_protos_dot_imageservice__pb2.StreamSummary.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'iamgestream.ImageStreamService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageStreamService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendImages(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/iamgestream.ImageStreamService/SendImages',
            futuracommon_dot_protos_dot_imageservice__pb2.ImageData.SerializeToString,
            futuracommon_dot_protos_dot_imageservice__pb2.StreamSummary.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)