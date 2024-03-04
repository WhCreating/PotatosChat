import servers_create as ser 
import client_system as clie

print("         Potatos Chat vBeta\n Комманды для чата:\n Создать чат - create \n Присоединиться к чату - join \n Выйти из чата - exit \n")
while True:
    a = input("Ввести комманду: ")
    if a == 'exit':
        break
    if a == 'create':
        addSearh = str(input("Введите ip адрес: "))
        portSearh = int(input("Введите порт: "))
        kolvo = int(input("Введите допустимое количество участников: "))
        ser.create_servers_method(addSearh, portSearh, kolvo)
    if a == "join":
        add = str(input("Введите IP адресс: "))
        porh = int(input("Введите порт: "))
        clie.join_client(add, porh)
    
        
    
    
    