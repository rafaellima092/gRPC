import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except Exception as e:
            print("Error receiving message:", e)
            break

def main():
    host = '127.0.0.1'
    port = 6969

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Solicitar ao usuário que insira um apelido
    nickname = input("Digite seu apelido: ")
    client_socket.send(nickname.encode())

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        client_socket.send(message.encode())

if __name__ == "__main__":
    main()
