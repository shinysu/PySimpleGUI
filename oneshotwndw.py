import PySimpleGUI as sg

lst=[ ]
layout = [
        [sg.Text('Enter your name'),sg.InputText("", key='name')],
        [sg.Button("Add"),sg.Button('Exit')],
        ]
window = sg.Window('My first GUI', layout)

button, values = window.Read()
if button == 'Add':
    lst.append(values['name'])

sg.Popup('Names are:',lst)
