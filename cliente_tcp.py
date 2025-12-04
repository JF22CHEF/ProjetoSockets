import socket
import time

def requisitar_service(nome):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("120.12.26.0", 2330))
    client_socket.send(f"resolva {nome}".encode())
    request = client_socket.recv(1024).decode()
    client_socket.close()
    return request

resposta = requisitar_service("calculadora_TCP")
if resposta[0] == "Não encontrado":
    print("Este serviço não foi encontrado aqui")

nome, ip, porta = resposta.split()
porta = int(porta)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, porta))

inicio = time.time()
client_socket.send("18 32".encode())
resultado = client_socket.recv(1024).decode()
fim = time.time()

print("Resultado: ", resultado)
print("Tempo total: ", fim - inicio)
