import socket
import threading
import pickle
from time import sleep, perf_counter
import PySimpleGUI as sg

#Userdefined modules
from IDEA.key_generation import create_key
from IDEA.idea_algorithm import operate

from GUI.gui_interface import create_gui

HEADERSIZE = 10
HOST = socket.gethostname()
PORT = 7890

USERNAME = sg.PopupGetText("Enter username:", no_titlebar=True)
if USERNAME == "" or USERNAME is None:
    exit()

keys = create_key()
ENCRYPTION_KEY = keys['encryption_key']
DECRYPTION_KEY = keys['decryption_key']

clients_information_list = dict()
clients_messages = dict()
clients_list = list()

launch = True
current_selected_user = ""

def transfrom_json_to_bytes(data):
    json_data = pickle.dumps(data)
    return bytes(f"{len(json_data):<{HEADERSIZE}}", 'utf-8') + json_data

def receive_message():
    global clients_information_list, clients_list, win, launch, current_selected_user
    while True:
        try:
            start = perf_counter()
            full_message = b''
            new_msg = True

            while True:
                msg = client_socket.recv(512)
                if new_msg:
                    msglen = int(msg[:HEADERSIZE])
                    new_msg = False

                full_message += msg

                if len(full_message)-HEADERSIZE == msglen:
                    new_msg = True
                    break
            data = pickle.loads(full_message[HEADERSIZE:])

            if data['type'] == 'status':
                clients_information_list = data['clients_information_list']
                clients_list = []
                for client in clients_information_list:
                    if client != USERNAME:
                        clients_list.append(client)
                        if client not in clients_messages:
                            clients_messages[client] = "---Start sending messages---\n"
                if not launch:
                    win['selected_user'].update(clients_list)
            else:
                if data['encryption'] == 'IDEA encryption':
                    message = operate(data['body'], DECRYPTION_KEY)
                else:
                    message = data['body']
                clients_messages[data['from']] += f"{data['from']}: {message}\n"

                if not launch and current_selected_user == data['from']:
                    win['message_box'].update(clients_messages[current_selected_user])
            end = perf_counter()
            print(f"Elapsed time to send (with encryption if any): {end-start}")

            if launch:
                launch = False
        except:
            print("closed")
            client_socket.close()
            break

def send_message(send_to_user, message, encryption):
    global clients_information_list, win, current_selected_user, clients_messages, launch
    start = perf_counter()
    clients_messages[send_to_user] += f"{USERNAME}: {message}\n"
    if encryption == 'IDEA encryption':
        message = operate(message, clients_information_list[send_to_user]['key'])
    clients_messages[send_to_user] += f"{USERNAME}: {message}\n"
    data = {
        'type': 'message',
        'to': send_to_user,
        'from': USERNAME,
        'encryption': encryption,
        'body': message
    }
    client_socket.send(transfrom_json_to_bytes(data))
    if not launch and current_selected_user == send_to_user:
        win['message_box'].update(clients_messages[current_selected_user])
    end = perf_counter()
    print(f"Elapsed time to send (with encryption if any): {end-start}")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_information = {
    'username': USERNAME,
    'key': ENCRYPTION_KEY
}
client_socket.send(transfrom_json_to_bytes(client_information))

win = create_gui("Welcome to Chat Application", clients_list, USERNAME)

if launch:
    receive_thread = threading.Thread(target=receive_message)
    receive_thread.start()
    launch = False


while True:
    event, values = win.read()

    if event == 'EXIT' or event == sg.WIN_CLOSED:
        client_socket.close()
        break

    if event == "selected_user":
        current_selected_user = values["selected_user"][0]
        win["message_box"].update(clients_messages[current_selected_user])
        win['input_message'].update(disabled=False)
        win['Send'].update(disabled=False)

    if event == 'Send' and values['input_message'] != '':
        if  current_selected_user != "":
            send_message(current_selected_user, values['input_message'], values['encryption'])
            win["input_message"].update("")

win.close()