import ext
import time
import termcolor as tc
import sys
import os

vars = {'sys': 'zx@cmd'}
nt = sys.argv[1]

def crash():
    eval('^[[C')

def read(file):
    f = ext.readFile(file)
    for l in f:
        z = l.split('##')
        if True:
        #try:
            if z[0] == 'echo':
                print(vars[z[1]])
            elif z[0] == 'sys':
                os.system(vars[z[1]])
            elif z[0] == 'wait':
                time.sleep(int(vars[z[1]]))
            elif z[0][0] == '#' or z[0] == '':
                pass
            elif z[0] == 'exit':
                input('Press [ENTER] to quit')
            elif z[0] == 'var':
                vars.update({z[1]:z[2]})
            elif z[0] == 'input':
                i = input()
                if i.lower == 'stop':
                    crash()
                vars.update({z[1]:i})
            elif z[0] == 'eval':
                i = eval(vars[z[1]])
                vars.update({z[1]:i})
            elif z[0] == 'loop':
                read(file)
            elif z[0] == 'equal':
                if vars[z[2]] == vars[z[3]]:
                    i = True
                else:
                    i = False
                vars.update({z[1]:i})
            else:
                print(tc.colored(f'{z[0]} must be a function'))

read(nt)
#except:
#    print(tc.colored(f'A error has occured while running {z[0]}'))