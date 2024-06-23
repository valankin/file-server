import socket

def send_text_to_server(text, host, port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(text.encode('utf-8'))
        response = client_socket.recv(1024)
        print('Received from server:', response.decode('utf-8'))

if __name__ == '__main__':

    # server_ip = input("Enter the server IP address: ")
    server_ip = '185.14.30.137'
    text_to_send = input("Enter text to send to the server: ")
    send_text_to_server(text_to_send, server_ip)

