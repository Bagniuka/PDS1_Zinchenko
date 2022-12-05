import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect(('localhost', 55555))
    while True:
        message = input('Enter number: ')
        c.sendall(message.encode())
        message = c.recv(1024)
        print(message.decode())
