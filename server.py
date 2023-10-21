import socket
import threading

# Создаем сокет и настраиваем его
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 1234))
server_socket.listen(5)  # Максимальное количество клиентов в очереди

# Список для хранения подключенных клиентов
clients = []

def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Клиент {client_address}: {message}")

            # Отправляем сообщение всем клиентам, включая отправителя
            for client in clients:
                if client != client_socket:
                    client.send(f"Клиент {client_address}: {message}".encode())
        except Exception as e:
            print(e)
            break

print("Сервер запущен. Ожидание подключения клиентов...")

while True:
    client, addr = server_socket.accept()
    print(f"Подключено клиент: {addr}")
    clients.append(client)

    # Создаем отдельный поток для каждого клиента
    client_handler = threading.Thread(target=handle_client, args=(client, addr))
    client_handler.start()
