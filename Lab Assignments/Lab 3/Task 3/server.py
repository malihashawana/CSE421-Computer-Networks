import socket
import threading 

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

def client_handle(server_socket, client_address):
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

        else:
            vowels = 'aeiouAEIOU'
            count = 0
            for char in message:
                if char in vowels:
                    count += 1    

            if count == 0:
                response = "Not enough vowels"
            elif count <= 2:
                response = "Enough vowels I guess"
            else:
                response = "Too many vowels"  

            server_socket.send(response.encode(format))     

        print("Received:", message) 

    server_socket.close()

while True:
    server_socket, client_address = server.accept()
    thread = threading.Thread(target = client_handle, args = (server_socket, client_address))
    thread.start() 
