import pyttsx3
import PySimpleGUI as sg

engine = pyttsx3.init()

layout = [[sg.Text('Enter the text to speak:')],
          [sg.Input(key='-INPUT-')],
          [sg.Radio('Male', 'RADIO1', default=True, key='-MALE-'),
           sg.Radio('Female', 'RADIO1', key='-FEMALE-')],
          [sg.Button('Speak'), sg.Button('Exit')]]

window = sg.Window('Text to Speech', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Speak':
        text = values['-INPUT-']
        if values['-MALE-']:
            voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
        else:
            voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        engine.setProperty('voice', voice_id)
        engine.say(text)
        engine.runAndWait()

window.close()
engine.stop()
