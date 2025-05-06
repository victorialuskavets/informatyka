import socket

client_socket = socket.socket()
port = 25002
client_socket.connect(('localhost', port))
while True:
    data = input("input msg (q to quit):")

    client_socket.sendall(data.encode('utf-8'))
    if data.lower() == 'q':
        client_socket.close()
        break