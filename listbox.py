import PySimpleGUI as sg

layout = [[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))],
          [sg.Button("OK")]]
window = sg.Window('My first GUI', layout)

button, values = window.Read()
sg.Popup('The GUI returned:', button, values)