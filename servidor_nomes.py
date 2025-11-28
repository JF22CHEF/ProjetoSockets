import socket
from threading import Thread

service = { "calculadora_UDP": ("120.12.26.0", 2207),
            "calculadora_TCP": ("120.12.26.0", 2309)
        }

def handle_request(client_socket, client_addr):
    print(f"Conexão do {client_addr} ao servidor de nomes estabelecida")
    
    while True:
        dados = client_socket.recv(1024).decode()
        if not dados:
            break
        
        request = dados.split()
        if request[0] == "calculadora_UDP":
            host = service["calculadora_UDP"][0]
            port = service["calculadora_UDP"][1]
            resposta = f"{host} {port}"
            client_socket.send(resposta.encode())
        
        elif request[0] == "calculadora_TCP":
            host = service["calculadora_TCP"][0]
            port = service["calculadora_TCP"][1]
            resposta = f"{host} {port}"
            client_socket.send(resposta.encode())
        
        else:
            resposta = "O serviço não foi encontrado aqui"
            client_socket.send(resposta.encode())
    client_socket.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind("120.12.26.0", 2330)
servidor.listen()

while True:
    client_socket, client_addr = servidor.accept()
    Thread(target=handle_request, args=(client_socket, client_addr)).start()
