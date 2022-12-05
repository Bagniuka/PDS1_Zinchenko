import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 55500))
    s.listen(5)
    conn, addr = s.accept()
    while True:
        message = conn.recv(1024).decode()
        print('Client: ', message)
        message = input('Server: ')
        conn.sendall(message.encode())
