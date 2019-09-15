import PySimpleGUI as sg

header_list = ['name', 'roll no']

data = [['shiny','001'],['adh','002']]

layout = [[sg.Table(values=data,
                            headings=header_list,
                            max_col_width=25,
                            auto_size_columns=True,
                            justification='centre',
                           # alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))],
          [sg.Button('Exit')]]

window = sg.Window('My first GUI', layout)
button, values = window.Read()