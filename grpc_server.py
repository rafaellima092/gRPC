import grpc
from concurrent import futures
import time
import chat_pb2
import chat_pb2_grpc

# Lista para armazenar mensagens
MESSAGES = []

class ChatServicer(chat_pb2_grpc.ChatServicer):
    def SendMessage(self, request, context):
        global MESSAGES
        MESSAGES.append({"user_id": request.user_id, "message": request.message})
        return chat_pb2.MessageResponse(user_id=request.user_id, message="Message received.")

    def ReceiveMessages(self, request, context):
        global MESSAGES
        for message in MESSAGES:
            yield chat_pb2.MessageResponse(user_id=message["user_id"], message=message["message"])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(ChatServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started")
    try:
        while True:
            time.sleep(86400)  # Um dia em segundos
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()