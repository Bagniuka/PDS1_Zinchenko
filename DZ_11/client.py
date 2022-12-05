import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 55555))
    message = input('Enter message: ')
    s.sendall(message.encode())
    data = s.recv(1024).decode()
    print(f'Recieved: {data}')

# Запитати за числа, бітові дані, та декодінг і енкодінг
# попрацювать з htttp
