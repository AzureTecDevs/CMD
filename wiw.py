#import subprocess
#import sys
import PySimpleGUI as sg
#import ext
#import time

def main():
    menu = [ ['Reset', ['Watch 1', 'Watch 2'] ], ['Start/Stop', ['Watch 1 ', 'Watch 2 '] ], ['Window', ['About', 'Exit' ] ] ]
    l1 = [ [sg.Menu(menu)], [sg.Input(size=(40,0), key='_OUT_', disabled=True)] ]
    l2 = [ [sg.Input(size=(40,0), key='_OUT2_', disabled=True)] ]
    layout = [ [sg.Frame(layout=l1, title='Watch 1')], [sg.Frame(layout=l2, title='Watch 2')] ]

    window = sg.Window('Stopwatch', layout, finalize=True)
    z = 0
    z2 = 0
    ss = False
    s = False
    while True:
        event, values = window.Read(timeout=50)
        if event == 'Exit':
            break
        if s:
            z += 0.05
        if ss:
            z2 += 0.05
        window['_OUT_'].update(value=str(int(z)))
        window['_OUT2_'].update(value=str(int(z2)))
        if event == 'About':
            sg.popup('Description: A basic stopwatch that can:\n◼ Start/Stop Watches\n◼ Reset Watches\nAuthors: AzureTecDevs\nVersion: v1.0.0', title='Stopwatch - About', non_blocking=True)
        elif event == 'Watch 1 ':
            s = not s
        elif event == 'Watch 2 ':
            ss = not ss
        elif event == 'Watch 1':
            try:
                z = 0
                window['_OUT_'].update(value='0')
            except:
                pass
        elif event == 'Watch 2':
            try:
                z2 = 0
                window['_OUT2_'].update(value='0')
            except:
                pass

    window.Close()

if __name__ == '__main__':
    main()