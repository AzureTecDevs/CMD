import subprocess
import sys
import PySimpleGUI as sg
import ext
import os
from playsound import playsound

def main():
    menu = [ ['Sound', ['Load'] ], ['Window', ['About', 'Exit']] ]
    layout = [ [sg.Menu(menu)] ]
    window = sg.Window('Audio Player', layout, size=(300,0), icon='sys.ico')
    while True:
        event, values = window.Read()
        if event in (None, 'Exit'):
            break
        if event == 'About':
            sg.popup('Description: Plays MP3 & WAV Files\nAuthor: AzureTecDevs\nVersion: v1.0.0', title='Audio Player - About')
        if event == 'Load':
            fi = sg.popup_get_file('Choose sound to play', title='Audio Player', file_types = (('Audio Files', '*.wav *.mp3'),))
            playsound(fi)
    window.Close()

if __name__ == '__main__':
    main()