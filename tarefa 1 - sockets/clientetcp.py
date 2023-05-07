import socket

# Configurações do cliente
host = 'localhost'
port = 5002
server_adress = (host, port)

# Criação do socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(server_adress)

# Solicita a palavra para tradução
palavra = input("Digite uma palavra em português: ")

# Envia a palavra para o servidor
sock.sendall(palavra.encode())

# Recebe a tradução do servidor
traducao = sock.recv(1024).decode()

# Exibe a tradução para o usuário
print(traducao)

# Fecha a conexão com o servidor
sock.close()
