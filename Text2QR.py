import PySimpleGUI as sg
import qrcode

sg.theme('DarkTeal')

layout = [
    [sg.Text('Enter Text to generate code: '), sg.InputText()],
    [sg.Button('Create QR Code'), sg.Button('Exit')], 
    [sg.Image(key='-IMAGE-', size=(200, 150))]
]

window = sg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Create QR Code':
        data = values[0]
        if data:
            img = qrcode.make(data)
            img.save('qrcode.png')
            window['-IMAGE-'].update(filename='qrcode.png')

window.close()