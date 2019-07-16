import PySimpleGUI as sg

layout = [
  [sg.Text('This is what a Text Element looks like')],
]

window = sg.Window('My first GUI', layout)

button, values = window.Read()