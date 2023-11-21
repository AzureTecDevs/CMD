import term as t
import os
import time

class tab():
    list = []
    space = '█'
    sel = 0
    def render(self):
        os.system('clear')
        st = '  █  '.join(self.list)
        t.write(t.bgwhite + t.black + st)
        l = os.get_terminal_size()
        n = l[0]
        n = n - len(t.strip(st))
        d = ' '*n
        t.write(d)
        t.write(t.off + '\n')
    
    def selTab(self, tab):
        self.sel = tab
        self.list[tab] = t.bggreen + self.list[tab] + t.bgwhite
    def unSelTab(self, tab):
        self.list[tab] = t.bgwhite + self.list[tab]
        
    def newTab(self, name):
        self.list.append(name)
        
    def setTab(self, l):
        self.list = l

r = tab()
r.newTab('  Hello')
r.newTab('Tama')
r.newTab('Bye  ' + r.space)
r.selTab(1)
r.render()
time.sleep(1)
r.selTab(0)
r.unSelTab(1)
r.render()