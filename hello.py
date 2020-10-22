import PySimpleGUI as sg

layout=[
        [sg.Text('Hello!!')],
        [sg.Button("OK")],
        ]
window = sg.Window('My first GUI', layout)

button, values = window.Read()
