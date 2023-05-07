import socket

# Dicionário de traduções no contexto de redes de computadores
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
port = 5002
server_address = (host, port)

# Criação do socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)

sock.listen(1)
print(f"Servidor TCP ouvindo em {host}:{port}")

while True:
    # Aguarda conexão do cliente
    conn, addr = sock.accept()
    print(f"Cliente conectado: {addr[0]}:{addr[1]}")

    # Recebe a palavra do cliente
    palavra = conn.recv(1024).decode()
    print(f"Palavra recebida: {palavra}")

    # Verifica a tradução no dicionário
    if palavra in traducoes:
        traducao = traducoes[palavra]
        mensagem = f"Tradução do inglês: {traducao['ingles']}\n"
    else:
        mensagem = "Tradução não encontrada"

    # Envia a tradução para o cliente
    conn.sendall(mensagem.encode())

    # Fecha a conexão com o cliente
    conn.close()
