import PySimpleGUI as sg

layout = [[sg.Button('klik saya')]]

window = sg.Window('contoh program simple gui', layout)

while True: 
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'klik saya':
        print('tombol klik')

window.close()