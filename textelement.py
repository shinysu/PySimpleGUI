import PySimpleGUI as sg

layout = [[sg.InputText('Default text')]]
window = sg.Window('My first GUI', layout)

button, values = window.Read()
sg.Popup('The GUI returned:', button, values)