import socket

# Configurações do servidor TCP
HOST = 'localhost'  # Endereço do servidor
PORT = 5000         # Porta TCP

# Cria o socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
    tcp_socket.bind((HOST, PORT))
    tcp_socket.listen()
    print(f"Servidor TCP ouvindo na porta {PORT}...")
    
    while True:
        conn, addr = tcp_socket.accept()
        with conn:
            print(f"Conexão TCP estabelecida com {addr}")
            data = conn.recv(1024)
            if data:
                response = f"TCP: {data.decode()}"
                conn.sendall(response.encode())
                print(f"Resposta enviada: {response}")
