import socket

def requisitar_service(nome):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 4000))
    client_socket.send(f"{nome}".encode())
    request = client_socket.recv(1024).decode()
    client_socket.close()
    return request

resposta = requisitar_service("Qualquer_coisa")
print("Resposta do servidor de nomes: ", resposta)
