import socket


def create_servers_method(a, p, k):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.INADDR_ANY)
    sock.bind((a, p))
    sock.listen(k)

    while True:
        conn, client_adress = sock.accept()
        print(f"Подключился: {client_adress}")
        
        data = conn.recv(1024)
        mass = input("Отправить: ")
        if mass == "/exit":
            sock.close()
        else :
            conn.send(mass.encode("utf-8"))
        print(data.decode())
       
        
    