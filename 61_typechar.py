from optparse import Values
import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('your typechars appear here: '), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('show'), sg.Button('exit')]]

window = sg.Window('patern 2b', layout)

while True:                     
\6
    event, value = window.read()
    print(event, Values)
    if event == sg.WIN_CLOSED or event == 'exit':
        break
    if event == 'show':
        window['-output-'].update(Values['-in-'])

        window.close()