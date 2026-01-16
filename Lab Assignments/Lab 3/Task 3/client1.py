import socket

data = 64
port = 5050
format = 'utf-8' 
device_name = socket.gethostname()
client_ip = socket.gethostbyname(device_name)

socket_address = (client_ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(socket_address)

def send_message(msg):
    message = msg.encode(format)
    msg_length = len(message)
    msg_length_str = str(msg_length).encode(format)
    msg_length_str += b' ' * (data - len(msg_length_str)) 

    client.send(msg_length_str)
    client.send(message)

    sent_from_server = client.recv(data).decode(format)
    print(f"Server response: {sent_from_server}")

while True:
    msg = input("Enter a message: ")
    send_message(msg) 
    if msg == "disconnect": 
        break 
    
client.close() 