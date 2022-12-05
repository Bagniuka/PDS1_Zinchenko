import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 55555))
    s.listen(5)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024).decode()
        spl_data = str(len(data.split(' ')))
        conn.sendall(spl_data.encode())
