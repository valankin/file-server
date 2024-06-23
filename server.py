import socket

def start_server(host='0.0.0.0', port=65432, file_path='received_text.txt'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if not data:
                    break
                with open(file_path, 'a') as file:
                    file.write(data.decode('utf-8') + '\n')
                conn.sendall(b'Text received and written to file.')

if __name__ == '__main__':
    start_server()

