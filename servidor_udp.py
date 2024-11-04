import socket

# Configurações do servidor UDP
HOST = 'localhost'  # Endereço do servidor
PORT = 5001         # Porta UDP

# Cria o socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
    udp_socket.bind((HOST, PORT))
    print(f"Servidor UDP ouvindo na porta {PORT}...")
    
    while True:
        data, addr = udp_socket.recvfrom(1024)
        if data:
            response = f"UDP: {data.decode()}"
            udp_socket.sendto(response.encode(), addr)
            print(f"Resposta enviada para {addr}: {response}")
