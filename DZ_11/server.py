import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('', 50667))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        print('conected')
        data = conn.recv(1024)
        print(data.decode('utf-8'))
        conn.send(input('Server: ').encode('utf-8'))