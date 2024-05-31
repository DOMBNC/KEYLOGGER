import socket
import time

def get_keyboard_input():
    server_address = ('192.168.1.27', 65432)  # Replace with the actual server IP and port
  
        
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server
        sock.connect(server_address)
    
        print(f"Connected to {server_address}")

        while True:
            # Capture keyboard input
            keyboard_input = input("Enter something: ")
            if keyboard_input.lower() == 'exit':
                print("Exiting the client...")
                break
            # Send the input to the server
            sock.sendall(keyboard_input.encode('utf-8'))
            print(f"Sent: {keyboard_input}")

            # Optional: Receive response from the server
            data = sock.recv(1024)
            print(f"Received: {data.decode('utf-8')}")

            # Sleep for a short period to avoid overwhelming the server
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        sock.close()
        print("Connection closed")

# Example usage
if __name__ == "__main__":
    get_keyboard_input()
