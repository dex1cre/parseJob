# -*- coding: utf-8 -*- 
import socket
import urllib.parse as pr_qs
import parse
import save_to_file
import config

def send_answer(conn, status="200 OK", typ="text/html; charset=utf-8", data=""):
    try:
        data = data.encode('utf-8')
        conn.send(b'HTTP/1.1 ' + status.encode("utf-8") + b"\r\n")
#    conn.send(b'Server: simplehttp\r\n')
        conn.send(b'Connection: close\r\n')
        conn.send(b'Content-Type: ' + typ.encode('utf-8') + b'\r\n')
        conn.send(b'Content-Length: ' + bytes(len(data)) + b'\r\n')
        conn.send(b'\r\n')
        conn.send(data)
    except:
        print("Error to send request")

def write_x():
    try:
        x = int(input("Print number of port: "))
    except:
        write_x()
    else:
        return x

def parse_dt(dt):
    try:
        if dt[5] == "?":
            x = ""
            for i in dt[6::]:
                if i != " ":
                    x = x + i
                else:
                    break
            return x
        else:
            return "favicon"
    except:
        print("Error to parse url")

def main():
    sock = socket.socket()
    sock.bind(("", write_x()))
    sock.listen(100)

    try:
        while 1:
            conn, addr = sock.accept()
            print("New connection from " + addr[0])
#            data = conn.recv(10204).decode('utf-8')
#            print("\n", data, "\n")
            dt = conn.recv(10240).decode('utf-8')
            xt =  pr_qs.parse_qs(parse_dt(dt))
            x = ""
            for i in xt:
                x = xt[i][0]
            if x != "":
                olny_to_return = save_to_file.write_to_file(parse.parse(parse.get_html(config.url), x))

            data = open('index.html', 'r').read()
            send_answer(conn=conn, data=data)
            conn.close()
    finally:
        sock.close()

if __name__ == "__main__":
    main()
