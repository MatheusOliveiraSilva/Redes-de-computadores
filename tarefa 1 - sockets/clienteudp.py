import socket

# Configurações do cliente
host = 'localhost'
port = 5001
server_address = (host, port)

# Cria um socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Solicita uma palavra em português para tradução
    palavra = input("Digite uma palavra em português: ")

    # Envia a palavra para o servidor
    sock.sendto(palavra.encode(), server_address)

    # Recebe a resposta do servidor
    data, server = sock.recvfrom(1024)
    traducao = data.decode()

    # Exibe a tradução no cliente
    print(f"A tradução da palavra é: {traducao}")

finally:
    # Fecha o socket
    sock.close()
