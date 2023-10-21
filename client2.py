import socket
import threading

# Создаем сокет и подключаемся к серверу
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 1234))

def receive_messages():
    while True:
        message = client_socket.recv(1024).decode()
        print("Сервер: " + message)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input("Вы: ")
    client_socket.send(message.encode())
