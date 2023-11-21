import PySimpleGUI as sg
import ext


def main():
    # App Info
    
    name = 'Custom App' # Name of app
    description = '' # App's description (used in About menu)
    version = '1.0.0' # App's version code (must be String)
    author = '' # Person/People who programmed your app
    
    # END
    menu = [['Window', ['About', 'Exit']]] # DO NOT DELETE Window MENU
    layout = [ [sg.Menu(menu)] ] # DO NOT REMOVE sg.Menu(menu)

    window = sg.Window(f'{name}', layout, size=(600,600)) # DO NOT DELETE
    while True:
        event, values = window.Read()
        if event in (None, 'Exit'): #DO NOT DELETE 
            break
        elif event == 'About': # DO NOT DELETE
            sg.popup(f'Description: {description}\nAuthor: {author}\nVersion: v{version}', title=f'{name} - About')
            
    window.Close()

if __name__ == '__main__':
    main()
