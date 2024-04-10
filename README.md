Para rodar é necessário instalar a biblioteca grpcio-tools
pip install grpcio-tools
rodar os arquivos grpc_server.py e grpc_client.py em terminais diferentes.
para rodar o arquivo chat.proto
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. chat.proto
