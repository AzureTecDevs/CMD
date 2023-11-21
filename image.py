import subprocess
import sys
import PySimpleGUI as sg
import ext
import os

def main():
    menu = [ ['Image', ['Load'] ], ['Window', ['About', 'Exit']] ]
    layout = [ [sg.Menu(menu)], [sg.Image('term2.png', key='_IMG_', expand_x=True, expand_y=True)] ]
    window = sg.Window('Gallery', layout, size=(300,300), icon='sys.ico', resizable=True)
    while True:
        event, values = window.Read()
        if event in (None, 'Exit'):
            break
        if event == 'About':
            sg.popup('Description: Image Viewer\nAuthor: AzureTecDevs\nVersion: v1.0.0', title='Gallery - About')
        if event == 'Load':
            img = sg.popup_get_file('Choose image to view', title='Gallery', file_types = (('PNG Files', '*.png'),))
            window['_IMG_'].update(filename=img)
    window.Close()

if __name__ == '__main__':
    main()