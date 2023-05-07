import socket

# Dicionário de traduções
traducoes = {
    'enlace': {'ingles': 'link', 'espanhol': 'enlace'},
    'comutadores': {'ingles': 'switches', 'espanhol': 'interruptores'},
    'roteador': {'ingles': 'router', 'espanhol': 'enrutador'},
    'pacote': {'ingles': 'packet', 'espanhol': 'paquete'},
    'provedor': {'ingles': 'provider', 'espanhol': 'proveedor'},
    'transmissão': {'ingles': 'broadcast', 'espanhol': 'transmisión'},
    'propagação': {'ingles': 'propagation', 'espanhol': 'propagación'},
    'cliente': {'ingles': 'client', 'espanhol': 'cliente'},
    'servidor': {'ingles': 'server', 'espanhol': 'servidor'},
    'protocolo': {'ingles': 'protocol', 'espanhol': 'protocolo'},
}

# Configurações do servidor
host = 'localhost'
port = 5001
server_address = (host, port)

# Criação do socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

print(f"Servidor UDP ouvindo em {host}:{port}")

while True:
    # Recebe a palavra do cliente
    data, address = sock.recvfrom(1024)
    palavra = data.decode()
    print(f"Palavra recebida: {palavra}")

    # Procura a tradução da palavra
    if palavra in traducoes:
        traducao = traducoes[palavra]
        mensagem = f"Tradução do inglês: {traducao['ingles']}\n"
    else:
        mensagem = 'Tradução não encontrada'

    # Envia a tradução para o cliente
    sock.sendto(mensagem.encode(), address)
