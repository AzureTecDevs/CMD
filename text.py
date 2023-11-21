import subprocess
import sys
import PySimpleGUI as sg
import ext


def main():
    menu = [['File', ['Save', 'Open', 'New']], ['Window', ['About', 'Exit']]]
    layout = [ [sg.Menu(menu)], [sg.MLine(key='_IN_', size=(40,15))] ]

    window = sg.Window('Text Pad', layout)
    while True:
        event, values = window.Read()
        if event in (None, 'Exit'):
            break
        elif event == 'About':
            sg.popup('Description: A text editor\nAuthor: AzureTecDevs\nVersion: v1.0.0', title='Text Pad - About')
        elif event == 'New':
            try:
                t = sg.popup_yes_no('Are you sure? Any changes you have made will be lost.', title='Text Pad')
                if t == 'Yes':
                    window['_IN_'].update(value='')
            except:
                pass
        elif event == 'Open':
            f = sg.popup_get_file('Select File', title='Text Pad', modal=False)
            window['_IN_'].update(value=''.join(ext.readFile(f)))
        elif event == 'Save':
            f = open(sg.popup_get_file('Select File', title='Text Pad'), 'w')
            f.write(window['_IN_'].get())
            f.close()
#        elif event == 'Save Output':
#            f = open(sg.popup_get_file('Select File', title='Text Pad'), 'w')
#            f.write(window['_OUT_'].get())
#            f.close()
#        elif event == 'Run as Python3':
#            try:
#                exec(window['_IN_'].get())
#            except:
#                print('error')
# Moved to idle.py
    window.Close()

if __name__ == '__main__':
    main()