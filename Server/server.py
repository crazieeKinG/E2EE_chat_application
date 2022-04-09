import socket
import threading
import pickle

HEADERSIZE = 10
HOST = socket.gethostname()
PORT = 7890

clients_socket_list = dict()
clients_information_list = dict()

def transfrom_json_to_bytes(data):
    json_data = pickle.dumps(data)
    return bytes(f"{len(json_data):<{HEADERSIZE}}", 'utf-8') + json_data

def receive_client():
    global client_socket_list
    while True:
        client_socket, address = server_socket.accept()

        client_information = receive_message(client_socket)
        username = client_information['username']
        print(f"Client connected: {address} AS {username}")

        clients_information_list[username] = client_information
        clients_socket_list[username] = client_socket

        broadcast_client_information(username, f'{username} joined the server!!')

        client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
        client_thread.start()

def handle_client(client, username):
    while True:
        try:
            message = receive_message(client)
            send_message(message['to'], transfrom_json_to_bytes(message))
        except:   
            clients_information_list.pop(username)         
            clients_socket_list.pop(username)         
            print(f"Client disconnected: {username}")
            broadcast_client_information(username, f'{username} left the server!!')
            break

def send_message(send_to_client_username, message):
    clients_socket_list[send_to_client_username].send(message)

def broadcast_client_information(username, message):
    data = {
            'type': 'status',
            'from': username,
            'body': message,
            'clients_information_list': clients_information_list
        }
    for client in clients_socket_list:
        clients_socket_list[client].send(transfrom_json_to_bytes(data))

def receive_message(client):
    full_message = b''
    new_msg = True
    while True:
        msg = client.recv(512)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_message += msg

        if len(full_message)-HEADERSIZE == msglen:
            new_msg = True
            break
    return pickle.loads(full_message[HEADERSIZE:])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
print(f"Server initiatied - {HOST}:{PORT}")

server_socket.listen(5)
print ("Socket is listening") 

receive_client()
