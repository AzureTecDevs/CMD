#!/usr/bin/env python
import sys
import os
import PySimpleGUI as sg

def main():
    folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAX5JREFUSEu11b9Lw0AUwPFvRdDBv6GDiJZC4zloEQVBEKstOAgdxLH+AEc3B+E2Z5cuOggFxUGsCK1g3QVBI/5qFRcRwcFFcLORS3NCl1woaZYM9+7z3rtwLxHa9ETa5KLhCpA0JHkDRoDvIMUoeLVUIJ9K+4dXaxBLsgssGWBHrSt48/oMacX8w+sOjGdwPj75QW11t4PjNBD9vH9R+XXIuvDVATLR5w87deiMQkcXRDxYof9JvESlY0ivsObCl9vIeNTQYDf0jJpP174DMcZG4yhOkIPD3sHovtTbq8I9sw5v3WDb9yAmPNi+QFpxczVBIuwHEJMaPjd/vCCoirEfQUxpuBwyPKPh0xDhJxAZDReR1kDQZv3j7CqIOQ0fIa3+EOF5DR+GCNdAZDW8j7QMNy9oP/YziAUNF0KEX0AsevDNDjLRG7Qm/7jbVxjKNeBULk1pa7l5SrWSRk2A9TzslZnVk0EN+elg06AppbK0oSdLUV3Atv+aWuncd88fvXR3feV8TRUAAAAASUVORK5CYII='
    file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAn1JREFUSEud1c9PE0EUB/DvWmRbwB+0rC1QLE24ePBC4tXoyRITohFIlJPJaEj0wtF48WTiH2BMNB7lYhMTQyre9NCj0Wi8iAHEtmy7bH/uz9ntrtkSkMUpls5td+Z93su82VkO/nEMwCyABADuwNzBxyeHzfuCg8HgWjqdTiYSCXAcB9d14bguLMuGppsolav4uZHHQDCA+3dvfwRwqR2+H76ZzWaXEskJmJT61jcdF9SyoGgGREnG2HAMnKVgcnLyA4DLLHw//IJaFsmLErMIx3FALRuKqqOvLwT+eACba6tIpVLLlNLrAOz9gT7YNCkpyZW2W+fhpmXDdb0GuOgJBPD962fMzc0u67ruw32wYZikXKsf2jPHcfHjVwHnknE0VA09PQF8+/IJszMzK5TSqd1gH6zpBlFU7VDYq9a2bYhyDf0hHpZtQzcoMpl3ePRg8TGAhx7ggxVNJ6bpb1y7LM1ms7UtDVXHVknG6noOC/PTLwGQf2FVI5bd/M/x/Tvt4dTeaai4XcXFC+fZcL2htrJ1PlzsHsWGomFiPM6Gq/UG8Tp91OGdFlU3MHxmiA2Xq3USCvJHdVtfqKoZECKn2bBcqZH+vtCRYS/AO01D4TawJFfIqRMDXcG1hgIhMsiuuCiVSXjwZFdwuVJHVAiz4a3SNhEig13B23IFsXbNK4gSiQqRruCiJGMkJrArzhWKZCQmdAUXRAnxkSgb3syJZGw02hX8O1/E2XiMCd9Kv3n76urUFfC9vQDcDhNwrR9DZuU9blybngewdPCuAM/z60+fPR8fHYt3iO4sy+fyuLdwZ8M0zSTr2vTeeT/TOQB7CzrMsA7gNYC9G+wPLKkwJvrTQQkAAAAASUVORK5CYII=76'
    
    starting_path = os.getcwd()
    
    #if not starting_path:
    #    sys.exit(0)
    treedata = sg.TreeData()
    
    def add_files_in_folder(parent, dirname):
        files = os.listdir(dirname)
        for f in files:
            fullname = os.path.join(dirname, f)
            if os.path.isdir(fullname):            # if it's a folder, add folder and recurse
                treedata.Insert(parent, fullname, f, values=[], icon=folder_icon)
                add_files_in_folder(fullname, fullname)
            else:
                treedata.Insert(parent, fullname, f, values=[fullname.split('.')[-1], os.stat(fullname).st_size], icon=file_icon)
    
    add_files_in_folder('', starting_path)
    menu = [['Window', ['About', 'Exit']]]
    layout = [[sg.Menu(menu)],
              [sg.Tree(data=treedata,
                       headings=['Type', 'Size'],
                       auto_size_columns=False,
                       select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
                       num_rows=20,
                       col0_width=25,
                       key='-TREE-',
                       show_expanded=False,
                       enable_events=True,
                       expand_x=True,
                       expand_y=True,
                       )]]
    
    window = sg.Window('File Viewer', layout, resizable=True, size=(700,600), finalize=True, titlebar_icon='term2.png')
    
    while True:     # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'About':
            sg.popup('Description: File/Folder Viewer\nAuthor: AzureTecDevs\nVersion: v1.0.0\nDirrectory: /', title='File Viewer - About')
        print(event, values)
    window.close()

if __name__ == '__main__':
    main()