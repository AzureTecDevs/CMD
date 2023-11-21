import ext
import time
import termcolor as tc
import sys
import os
import term as t
import climage 

v = {'sys': 'zx@cmd'}

def render(sel):
    os.system('clear')
    if sel == 1:
        st = t.bggreen + '  ASM  ' + t.bgwhite + '▉  Help  ▉'
    elif sel == 2:
        st = t.bgwhite + '  ASM  ▉' + t.bggreen + '  Help  ' + t.bgwhite + '▉'
    ver = 'v1.0.0'
    t.write(t.bgwhite + t.black + st)
    l = os.get_terminal_size()
    n = l[0]
    n = n - len(t.strip(st))
    tm = l[0]
    tm = tm - len(t.strip(ver))
    d = ' '*n
    t.write(d)
    t.pos(0,tm)
    t.write(ver)
    t.write(t.off + '\n')

class crashError(Exception):
    def __init__(self, message="Sucsessfully Crashed ASM"):
        self.message = message
        super().__init__(self.message)

def crash():
    raise crashError

def read(file):
    log = []
    f = ext.readFile(file)
    for l in f:
        n = l.split(',,')
        a = n[0].lower
        #if True:
        try:
            def run(z):
                if z[0] == 'dec':
                    v.update({z[1] : z[2]})
                elif z[0] == 'srt':
                    print(v[z[1]])
                elif z[0] == 'ctm':
                    time.sleep(int(v[z[1]]))
                elif z[0] == 'img':
                    print(climage.convert(f'img/{v[z[1]]}.png'))
                elif z[0] == 'if':
                    if v[z[1]] == v[z[2]]:
                        log.append(tc.colored(f'Logger : IF statment ran , True , {z[3:]}', 'green'))
                        run(z[3:])
                    else:
                        log.append(tc.colored(f'Logger : IF statment ran , False , {z[3:]}', 'green'))
                elif z[0] == 'clr':
                    os.system('clear')
                    render(1)
                elif z[0] == 'sra':
                    t.saveCursor()
                    t.pos(v[z[3]], v[z[2]])
                    t.write(str(v[z[1]]))
                    t.restoreCursor()
                elif z[0] == 'eval':
                    v.update({z[2] : eval(v[z[1]])})
                elif z[0] == 'in':
                    i = input('> ')
                    v.update({z[1] : i})
                elif z[0] == 'loop':
                    return True
                elif z[0] == 'crh':
                    crash()
                elif z[0].startswith(';') or z[0].startswith(' ') or z[0].startswith(''):
                    return False
                else:
                    print(tc.colored(f'A error has occured while running {file} : "{z[0]}" isn\'t a command', 'red'))
                    return False
                    
                log.append(tc.colored(f'Logger : {z[0]} , {z}', 'green'))
            is_loop = run(n)
            if is_loop:
                read(file)
        except:
            print(tc.colored(f'A error has occured while running {file}', 'red'))
    print('\n'.join(log))
    
render(1)
doc = 1
print('Use \'help\' to switch to HELP tab')
while True:
    if doc == 1:
        nt = input(tc.colored('ASM $ ', 'blue'))
        #if True:
        try:
            if nt == 'help':
                doc = 2
            else:
                read(nt)
        except:
            print(tc.colored(f'A error has occured while loading {nt}', 'red'))
    else:
        render(2)
        print(f'''ASM Help Menu
Written for: v1.0.0

{t.bold}ASM Commands{t.off}
dec,,<var>,,<val> : set/create variable <var> to value <val>
srt,,<var> : echo value of <var> to terminal
sra,,<var>,,<x>,,<y> : same as srt, but echos at <x>,<y>
img,,<file> : echo png file <file> to termial
ctm,,<var> : wait for <var> seconds (variable must be integer)
eval,,<in>,,<out> : evaluate <in>, then store result to <out>
in,,<var> : store user\'s input to variable <var>
if,,<s1>,,<s2>,,<cmd> : check if variables <s1> and <s2> are equal, then run <cmd>''')
        auth = 'By: AzureTecDevs'
        l = os.get_terminal_size()
        mx = l[0]
        mx = mx - len(t.strip(auth))
        t.pos(3,mx)
        t.write(auth)
        t.pos(l[1], l[0])
        input()
        doc = 1
        render(1)