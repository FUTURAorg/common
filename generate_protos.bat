@echo off

for %%a in (futuracommon/protos/*.proto) do (
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./futuracommon/protos/%%a
)