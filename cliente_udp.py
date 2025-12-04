import socket
import time

def requisitar_service(nome):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.connect(("127.0.0.1", 2330))
    client_socket.send(f"resolva {nome}".encode())
    request = client_socket.recv(1024).decode()
    client_socket.close()
    return request

resposta = requisitar_service("calculadora_UDP")
if resposta[0] == "Não encontrado":
    print("Este serviço não foi encontrado aqui")

nome, ip, porta = resposta.split()
porta = int(porta)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

inicio = time.time()
client_socket.sendto("18 32".encode(), (ip, porta))
resultado, ender = client_socket.recvfrom(1024)
fim = time.time()

print("Resposta: ", resultado.decode())
print("Tempo total: ", fim - inicio)
