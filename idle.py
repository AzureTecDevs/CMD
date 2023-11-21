import subprocess
import sys
import PySimpleGUI as sg
import ext

def main():
    menu = [['File', ['Save', 'Save Output', 'Load', 'New']], ['Python', ['Run Script']], ['Window', ['About', 'Exit', 'Clear Output']]]
    l1 = [ [sg.Menu(menu)], [sg.MLine(key='_IN_', size=(40,15))] ]
    l2 = [ [sg.Output(size=(40,15), key='_OUT_')] ]
    input = sg.Tab("Edit Program", l1)
    output = sg.Tab("Program Output", l2)
    layout = [ [sg.TabGroup([[input, output]])] ]

    window = sg.Window('IDLE', layout, right_click_menu=menu)
    while True:
        event, values = window.Read()
        if event in (None, 'Exit'):
            break
        elif event == 'About':
            sg.popup('Description: IDLE (Intergrated Development Editor)\nAuthors: Python Software Foundation, AzureTecDevs\nVersion: v1.6.2', title='IDLE - About')
        elif event == 'New':
            try:
                t = sg.popup_yes_no('Are you sure? Any changes you have made will be lost.', title='IDLE')
                if t == 'Yes':
                    window['_IN_'].update(value='')
            except:
                pass
        elif event == 'Clear Output':
            try:
                window['_OUT_'].update(value='')
            except:
                pass
        elif event == 'Load':
            try:
                f = sg.popup_get_file('Select File', title='IDLE', file_types = (('Python Script', '*.py'),))
                window['_IN_'].update(value=''.join(ext.readFile(f)))
            except:
                pass
        elif event == 'Save':
            try:
                f = open(sg.popup_get_file('Select File', title='IDLE', save_as=True, file_types = (('Python Scripts', '*.py'),)), 'w')
                f.write(window['_IN_'].get())
                f.close()
            except:
                pass
        elif event == 'Save Output':
            try:
                f = open(sg.popup_get_file('Select File', title='IDLE', save_as=True, file_types = (('LOG Files', '*.log'),)), 'w')
                f.write(window['_OUT_'].get())
                f.close()
            except:
                pass
        elif event == 'Run Script':
            try:
                exec(window['_IN_'].get())
            except:
                print('A error has occured')

    window.Close()

if __name__ == '__main__':
    main()