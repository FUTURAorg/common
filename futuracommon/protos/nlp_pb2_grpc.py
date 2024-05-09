# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from futuracommon.protos import nlp_pb2 as futuracommon_dot_protos_dot_nlp__pb2


class NLPServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NotifySuccess = channel.unary_unary(
                '/nlp.NLPService/NotifySuccess',
                request_serializer=futuracommon_dot_protos_dot_nlp__pb2.SuccessNotification.SerializeToString,
                response_deserializer=futuracommon_dot_protos_dot_nlp__pb2.NotificationResponse.FromString,
                )


class NLPServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NotifySuccess(self, request, context):
        """A method to send a notification of a successful action
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NLPServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NotifySuccess': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifySuccess,
                    request_deserializer=futuracommon_dot_protos_dot_nlp__pb2.SuccessNotification.FromString,
                    response_serializer=futuracommon_dot_protos_dot_nlp__pb2.NotificationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nlp.NLPService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NLPService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NotifySuccess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nlp.NLPService/NotifySuccess',
            futuracommon_dot_protos_dot_nlp__pb2.SuccessNotification.SerializeToString,
            futuracommon_dot_protos_dot_nlp__pb2.NotificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
