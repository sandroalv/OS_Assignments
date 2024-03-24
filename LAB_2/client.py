import socket
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_to_server():
    server_address = ('localhost', 1234)
    try:
        client_socket.connect(server_address)
    except ConnectionRefusedError:
        print("Error: Unable to connect to the server.")
        sys.exit(1)

def add_item(item):
    try:
        client_socket.sendall(f'1 {item}'.encode())
        response = client_socket.recv(1024).decode()
        print(f'Server replied: {response}')
    except ConnectionError:
        print("Server has been terminated. Unable to add item.")
        sys.exit(0)

def retrieve_items():
    try:
        client_socket.sendall('2'.encode())
        response = client_socket.recv(1024).decode()
        if response.startswith('Server replied:'):
            print(f'{response}')
        else:
            print('Server has been shut down. Exiting...')
            sys.exit(0)
    except Exception as e:
        print(f'Error occurred: {str(e)}')
        sys.exit(0)

def main():
    connect_to_server()
    try:
        while True:
            print('1) Add item')
            print('2) Retrieve items')
            print('3) Exit')
            choice = input('What do you want to do? ')
            
            if choice == '1':
                item = input('What item do you want to add? ')
                add_item(item)
            elif choice == '2':
                retrieve_items()
            elif choice == '3':
                break
            else:
                print('Invalid choice. Please try again.')

    except KeyboardInterrupt:
        print('Exiting...')
    finally:
        client_socket.close()

if __name__ == '__main__':
    main()
