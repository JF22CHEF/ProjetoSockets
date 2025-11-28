import socket

def calculadora(expression):
    x, y = expression.split()
    x = float(x)
    y = float(y)
    
    if x and y:
        total = x + y
        return total
    else:
        return "Erro"

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("120.12.26.0", 2207))
resposta = "Isso aqui veio do servidor UDP"
print("O servidor UDP foi iniciado")

while True:
    dados, ender = servidor.recvfrom(1024)
    if not dados:
        break
    resultado = calculadora(dados)
    servidor.sendto(resposta.encode(), ender)
    servidor.sendto(str(resultado).encode(), ender)
