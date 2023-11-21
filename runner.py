import subprocess
import sys
import PySimpleGUI as sg
import ext
import os
import tkinter
app = tkinter.Tk()
wid = app.winfo_screenwidth() - 15
hit = app.winfo_screenheight()
app.destroy()

def main():
    menu = [ ['Programs', ['Text Pad', 'Linux Console', 'IDLE', 'Calculator', 'Gallery', 'Stopwatch', 'File Viewer', 'Contacts'] ], ['Custom Apps', ['1', '2', '3', '4', '5'] ], ['System', ['About', 'Help', 'Shut Off']] ]
    layout = [ [sg.Menu(menu)] ]
    window = sg.Window('App Launcher', layout, size=(wid,0), disable_close=True, icon='sys.ico', location=(0,0), no_titlebar=True, keep_on_top=True, modal=False)
    while True:
        event, values = window.Read()
        if event in (None, 'Shut Off'):
            break
        if event == 'Help':
            sg.popup('''
-------- Opening Apps -------
To open an app, go to Programs, then click on the app.

---- Opening Custom Apps ----
To open a custom app, go to Custom Apps, then click on the program\'s number (1-5)''', title='System - Help')
        if event == 'About':
            sg.popup('Description: CMD GUI Interface\nAuthor: AzureTecDevs\nVersion: v1.0.4', title='System - About')
        if event == 'Text Pad':     
            f = ''.join(ext.readFile('text.py'))
            exec(f)
        if event == 'Contacts':     
            f = ''.join(ext.readFile('contact.py'))
            exec(f)
        if event == 'Gallery':
            f = ''.join(ext.readFile('image.py'))
            exec(f)
        if event == 'Stopwatch':
            f = ''.join(ext.readFile('wiw.py'))
            exec(f)
        if event == 'File Viewer':
            f = ''.join(ext.readFile('tree.py'))
            exec(f)
        if event in ('1', '2', '3', '4', '5'):
            f = ''.join(ext.readFile(f'{event}.py'))
            exec(f)
        if event == 'Calculator':
            try:
                f = ''.join(ext.readFile('calc.py'))
                exec(f)
            except:
                print('A error has occured while running Calculator')
        if event == 'IDLE':
            try:
                f = ''.join(ext.readFile('idle.py'))
                exec(f)
            except:
                print('A error has occured while running IDLE')
        if event == 'Linux Console':
            f = ''.join(ext.readFile('console.py'))
            exec(f)

    window.Close()

if __name__ == '__main__':
    main()