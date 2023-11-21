import subprocess
import sys
import PySimpleGUI as sg

def main():
    menu = [['Terminal', ['Run']], ['Window', ['About', 'Exit']]]
    layout = [ [sg.Menu(menu)], [sg.Input(key='_IN_', size=(41,1))],[sg.Output(size=(40,15))],[sg.Button('Run')] ]

    window = sg.Window('Linux Console', layout, icon='term.ico')
    
    def runCommand(cmd, timeout=None, window=None):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ''
        for line in p.stdout:
            line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
            output += line
            print(line)
            window.Refresh() if window else None
        retval = p.wait(timeout)
        
    while True:
        event, values = window.Read()
        if event in (None, 'Exit'):
            break
        if event == 'About':
            sg.popup('Description: Linux Console\nAuthor: Louis Lietaer, AzureTecDevs\nVersion: v1.1.8', title='Linux Console - About')
        if event == 'Run':
            try:
                runCommand(cmd=values['_IN_'], window=window)
            except:
                print('An error has occured')

    window.Close()

if __name__ == '__main__':
    main()