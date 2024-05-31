import socket
import threading

def handle_client(client_socket):
    """ Function to handle client connections """
    file_path = '/home/kali/Desktop/file.txt'
    with open(file_path, 'a') as f:
        while True:
            try:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:
                    break
                # Print the received data
                message = data.decode('utf-8')
                print(f"Received: {message}")
                
                # Write the received data to file.txt
                f.write(message + '\n')

                # Send a response back to the client
                client_socket.sendall(f"Echo: {message}".encode('utf-8'))
            except Exception as e:
                print(f"An error occurred: {e}")
                break
    client_socket.close()

def start_server():
    """ Function to start the server on localhost and port number """
    server_address = ('0.0.0.0', 65432)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print(f"Server listening on {server_address}")
    print("Listening was successful")  # Added message to confirm successful listening

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
