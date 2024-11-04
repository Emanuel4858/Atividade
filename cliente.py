import socket

# Configurações do cliente
HOST = 'localhost'  # Endereço do servidor
TCP_PORT = 5000
UDP_PORT = 5001

def enviar_tcp(mensagem):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.connect((HOST, TCP_PORT))
        tcp_socket.sendall(mensagem.encode())
        resposta = tcp_socket.recv(1024).decode()
        print(f"Resposta do servidor: {resposta}")

def enviar_udp(mensagem):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.sendto(mensagem.encode(), (HOST, UDP_PORT))
        resposta, _ = udp_socket.recvfrom(1024)
        print(f"Resposta do servidor: {resposta.decode()}")

# Solicita o protocolo e a mensagem ao usuário
protocolo = input("Escolha o protocolo (TCP ou UDP): ").strip().upper()
mensagem = input("Digite a mensagem para o servidor: ")

if protocolo == "TCP":
    enviar_tcp(mensagem)
elif protocolo == "UDP":
    enviar_udp(mensagem)
else:
    print("Protocolo inválido.")
