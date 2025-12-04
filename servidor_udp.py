import socket
import threading

def registrar_nome():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect("127.0.0.1", 2330)
    mensagem = "registro calculadora_UDP 127.0.0.1 2207"
    server.send(mensagem.encode())
    server.recv(1024)
    server.close()

def calculadora(expression):
    x, y = expression.split()
    x = float(x)
    y = float(y)
    
    if x and y:
        total = x + y
        return total
    else:
        return "Erro"

def handle_client(client_socket):
    print(f"Conexão ao servidor UDP estabelecida")
    
    while True:
        dados, ender = client_socket.recvfrom(1024)
        if not dados:
            break
        
        resultado = calculadora(dados)
        client_socket.sendto(str(resultado).encode(), ender)
    client_socket.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("127.0.0.1", 2207))
print("O servidor UDP foi iniciado")

while True:
    threading.Thread(target=handle_client, args=(servidor,)).start()
