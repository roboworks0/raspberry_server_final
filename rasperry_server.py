import socket

HOST = 'localhost'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}")

client_socket, client_address = server_socket.accept()

while True:
    data = client_socket.recv(1024).decode()

    if not data:
        print("Client disconnected")
        break
    
    print(f"Received message : {data}")

client_socket.close()
server_socket.close()
