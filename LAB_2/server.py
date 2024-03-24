import socket
import threading
import sys
import signal

# Choose server address and port
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 1234

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)  # Up to 5 connection requests

print('Server started. Listening for connections')

# Define the shopping list
shopping_list = []

# Function to handle client requests
def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            if data.startswith('1'):
                item = data[2:]  # Extract the item from the command
                shopping_list.append(item)
                response = 'Server replied: Item added!'

            elif data == '2':
                response = f'Server replied: {shopping_list}'

            elif data == '3':
                response = 'Server: Shutting down'
                break

            client_socket.send(response.encode())

    except Exception as e:
        print(f'Error occurred: {str(e)}')

    finally:
        # Close the client connection
        client_socket.close()

def sigterm_handler(signum, frame):
    print("\nSIGTERM received. Creating backup...")
    # Save shopping_list to a backup file (overwrite existing content)
    with open('backup.txt', 'w') as backup_file:
        backup_file.write('\n'.join(shopping_list))
    print("Backup created. Shutting down server.")
    server_socket.close()
    sys.exit(0)


def main():
    global shopping_list  # Declare shopping_list as global
    shopping_list = []  # Initialize shopping_list

    signal.signal(signal.SIGTERM, sigterm_handler)

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f'New connection from {client_address}')

            # Handle the client in a separate thread
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.daemon = True   
            client_handler.start()

    except KeyboardInterrupt:
        print("\nServer shutting down. Creating backup...")
        # Save the shopping list to the backup file before exiting
        with open('backup.txt', 'w') as backup_file:
            backup_file.write('\n'.join(shopping_list))
        server_socket.close()
        sys.exit(0)


if __name__ == "__main__":
    main()