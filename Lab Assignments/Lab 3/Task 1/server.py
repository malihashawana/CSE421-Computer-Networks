import socket

port = 5050
format = 'utf-8'
data = 64
device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)

server_socket_address = (server_ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)

server.listen()
print(f"Server is listening...")

while True:
    server_socket, client_address = server.accept()
    print(f"Connected to {client_address}")

    connected = True

    while connected:
        upcoming_msg_length = server_socket.recv(data).decode(format)
        print(f"Received message length: {upcoming_msg_length.strip()}")

        msg_length = int(upcoming_msg_length.strip())
        message = server_socket.recv(msg_length).decode(format)

        if message == 'disconnect':
            print("Disconnected with client")
            connected = False

        print(message)
        server_socket.send("Message received".encode(format))

    server_socket.close()