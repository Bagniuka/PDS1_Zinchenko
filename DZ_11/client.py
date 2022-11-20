import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(('localhost', 50667))
    while True:
        client.send(input("Client: ").encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))
