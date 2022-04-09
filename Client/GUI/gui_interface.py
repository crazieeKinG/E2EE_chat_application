import PySimpleGUI as sg

def create_gui(displaymessages, client_list, current_user):
    input_section = [
        [
            sg.In(size=(55,1), enable_events=True, key="input_message", disabled=True), 
            sg.OK("Send", key="Send", disabled=True),
            sg.OptionMenu(['IDEA encryption', 'No encryption'], size=(15,1), default_value='IDEA encryption', key="encryption")
        ]
    ]

    layout = [
        [sg.Text("Messages", background_color='white', text_color='black')],
        [
            sg.Listbox(client_list, size=(10,25), key="selected_user", enable_events=True, background_color="white", highlight_background_color="grey"),
            sg.Column(layout=[[sg.Multiline(displaymessages, key="message_box", size=(65,25) , autoscroll=True, disabled=True, background_color='white', text_color='black')]], background_color='white')],
        [
            sg.Column(input_section, background_color='white')
        ]
    ]

    return sg.Window(f"Chat Application Using IDEA | Logged in: {current_user}", layout, background_color='white', finalize=True)