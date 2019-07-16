import PySimpleGUI as sg

layout = [[sg.InputCombo(['choice 1', 'choice 2'])],
          [sg.Button("OK")]]
window = sg.Window('My first GUI', layout)

button, values = window.Read()
sg.Popup('The GUI returned:', button, values)