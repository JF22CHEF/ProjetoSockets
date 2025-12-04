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
        if request[0] == "registro":
            nome = request[1]
            ip = request[2]
            port = request[3]
            port = int(request[3])
            service[nome] = (ip, port)
            client_socket.send("OK".encode())
        
        elif request[0] == "resolva":
            nome = request[1]
            if nome in service:
                ip, port = service[nome]
                resposta = f"{ip} {port}"
                client_socket.send(resposta.encode())
            else:
                client_socket.send("Não encontrado".encode())

    client_socket.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind("120.12.26.0", 2330)
servidor.listen()

while True:
    client_socket, client_addr = servidor.accept()
    Thread(target=handle_request, args=(client_socket, client_addr)).start()
