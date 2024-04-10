import socket
import threading

def broadcast(message, clients):
    for client in clients:
        try:
            client.send(message.encode())
        except Exception as e:
            print("Error broadcasting message:", e)

def handle_client(client_socket, clients):
    # Receber o apelido do cliente
    nickname = client_socket.recv(1024).decode()
    print(f"{nickname} entrou no chat.")
    
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                clients.remove(client_socket)
                client_socket.close()
                print(f"{nickname} saiu do chat.")
                break
            broadcast(f"{nickname}: {message}", clients)  # Aqui estamos enviando o apelido junto com a mensagem
        except Exception as e:
            print("Error:", e)
            break


def main():
    host = '127.0.0.1'
    port = 6969
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    
    print("Server listening on port", port)

    clients = []

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print("Connection from", addr)

        client_handler = threading.Thread(target=handle_client, args=(client_socket, clients))
        client_handler.start()

if __name__ == "__main__":
    main()
