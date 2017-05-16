import socket

def send_answer(conn, status="200 OK", typ="text/html; charset=utf-8", data=""):
    data = data.encode('utf-8')
    conn.send(b'HTTP/1.1 ' + status.encode("utf-8") + b"\r\n")
#    conn.send(b'Server: simplehttp\r\n')
    conn.send(b'Connection: close\r\n')
    conn.send(b'Content-Type: ' + typ.encode('utf-8') + b'\r\n')
    conn.send(b'Content-Length: ' + bytes(len(data)) + b'\r\n')
    conn.send(b'\r\n')
    conn.send(data)

def write_x():
    try:
        x = int(input("Print number of port: "))
    except:
        write_x()
    else:
        return x

def main():
    sock = socket.socket()
    sock.bind(("", write_x()))
    sock.listen(10)

    try:
        while 1:
            conn, addr = sock.accept()
            print("New connection from " + addr[0])
#            data = conn.recv(10204).decode('utf-8')
#            print("\n", data, "\n")
            dt = conn.recv(10240).decode('utf-8')
            print("\n", dt, "\n")
            data = open('index.html', 'r').read()
            send_answer(conn=conn, data=data)
            conn.close()
    finally:
        sock.close()

if __name__ == "__main__":
    main()
