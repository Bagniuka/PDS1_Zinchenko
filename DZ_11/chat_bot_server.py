import socket
import datetime as d

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 55000))
    s.listen(5)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if data == b"Time":
            time = str(d.datetime.now().time())
            conn.sendall(time.encode())
        elif data == b"Who is the most badass protagonist?":
            conn.sendall("John Wick".encode())
        elif data == b"Date":
            date = str(d.datetime.now().date())
            conn.sendall(date.encode())
