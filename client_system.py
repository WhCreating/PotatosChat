import socket


def join_client(a, p):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((a, p))
    while True:
        mass = input("Отправить: ")
        sock.send(mass.encode("utf-8"))
        data = sock.recv(1024)
        print(data.decode())
        sock.close()