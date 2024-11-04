import socket
import threading

# Configurações do servidor
HOST = 'localhost'    # Endereço do servidor
TCP_PORT = 5000       # Porta para conexões TCP
UDP_PORT = 5001       # Porta para conexões UDP

def handle_tcp_connection(conn, addr):
    """Função para tratar uma conexão TCP em uma nova thread"""
    with conn:
        print(f"Conexão TCP estabelecida com {addr}")
        data = conn.recv(1024)  # Recebe dados do cliente
        if data:
            response = f"TCP: {data.decode()}"  # Adiciona o prefixo "TCP:"
            conn.sendall(response.encode())     # Envia a resposta ao cliente
            print(f"Resposta enviada para {addr}: {response}")

def start_tcp_server():
    """Função para iniciar o servidor TCP e escutar conexões"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.bind((HOST, TCP_PORT))
        tcp_socket.listen()
        print(f"Servidor TCP ouvindo na porta {TCP_PORT}...")

        while True:
            conn, addr = tcp_socket.accept()  # Aceita uma nova conexão TCP
            # Cria uma nova thread para cada cliente TCP
            tcp_thread = threading.Thread(target=handle_tcp_connection, args=(conn, addr))
            tcp_thread.start()

def start_udp_server():
    """Função para iniciar o servidor UDP e processar mensagens"""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.bind((HOST, UDP_PORT))
        print(f"Servidor UDP ouvindo na porta {UDP_PORT}...")

        while True:
            data, addr = udp_socket.recvfrom(1024)  # Recebe dados e endereço do cliente
            if data:
                response = f"UDP: {data.decode()}"  # Adiciona o prefixo "UDP:"
                udp_socket.sendto(response.encode(), addr)  # Envia a resposta ao cliente
                print(f"Resposta enviada para {addr}: {response}")

# Inicia os servidores TCP e UDP em threads separadas
tcp_thread = threading.Thread(target=start_tcp_server)
udp_thread = threading.Thread(target=start_udp_server)

tcp_thread.start()
udp_thread.start()

tcp_thread.join()
udp_thread.join()
