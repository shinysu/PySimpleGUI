import PySimpleGUI as sg

l=[ ]
layout = [
        [sg.Text('Enter your name'),sg.InputText("", key='name')],
        [sg.Button("Add"),sg.Button('Exit')],
        ]
window = sg.Window('My first GUI', layout)
while True:
    button, values = window.Read()
    if button == 'Add':
        l.append(values['name'])
        window.FindElement('name').Update("")
    elif button == 'Exit':
        sg.Popup('Names are:', l)
        break
