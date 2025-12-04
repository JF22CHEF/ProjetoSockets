import socket
import threading

def registrar_nome():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect("120.12.26.0", 2330)
    mensagem = "registro calculadora_TCP 120.12.26.0 2309"
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

def handle_client(client_socket, client_addr):
    print(f"Conexão do {client_addr} ao servidor TCP estabelecida")
    
    while True:
        dados = client_socket.recv(1024).decode()
        if not dados:
            break
        
        resultado = calculadora(dados)
        client_socket.send(str(resultado).encode())
    client_socket.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("120.12.26.0", 2309))
servidor.listen()
print("O servidor TCP foi iniciado")

while True:
    client_socket, client_addr = servidor.accept()
    threading.Thread(target=handle_client, args=(client_socket, client_addr)).start()
