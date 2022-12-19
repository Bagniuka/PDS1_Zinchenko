import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 55000))
    while True:
        message = input('Client: ')
        s.sendall(message.encode())
        message = s.recv(1024).decode()
        print('Server: ', message)
