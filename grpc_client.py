import grpc
import chat_pb2
import chat_pb2_grpc
import threading

def send_message(stub, user_id, message):
    response = stub.SendMessage(chat_pb2.MessageRequest(user_id=user_id, message=message))
    print("Response:", response.message)

def receive_messages(stub, user_id):
    responses = stub.ReceiveMessages(chat_pb2.MessageRequest(user_id=user_id))
    for response in responses:
        print(f"{response.user_id}: {response.message}")

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_pb2_grpc.ChatStub(channel)
    user_id = input("Enter your user ID: ")

    # Iniciar uma thread para receber mensagens enquanto o usuário envia mensagens
    receive_thread = threading.Thread(target=receive_messages, args=(stub, user_id))
    receive_thread.start()

    while True:
        message = input("Enter message (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        send_message(stub, user_id, message)

    # Aguardar até que a thread de recebimento termine
    receive_thread.join()

    print("Exiting...")

if __name__ == '__main__':
    main()
