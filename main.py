import cmd
import os
import sys
import termcolor as tc
from ext import *
from time import sleep
import term

def start():
    print('sys1.0.0')
    term.pos(1,0)
    
def cipher():
    # Caesar Cipher

    MAX_KEY_SIZE = 26
    
    def getMode():
        while True:
            print('Do you wish to encrypt or decrypt a message?')
            mode = input().lower()
            if mode in 'encrypt e decrypt d'.split():
                return mode
            else:
                print('Enter either "encrypt" or "e" or "decrypt" or "d".')
    
    def getMessage():
        print('Enter your message:')
        return input()
    
    def getKey():
        key = 0
        while True:
            print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
            key = int(input())
            if (key >= 1 and key <= MAX_KEY_SIZE):
                return key
    
    def getTranslatedMessage(mode, message, key):
        if mode[0] == 'd':
            key = -key
        translated = ''
    
        for symbol in message:
            if symbol.isalpha():
                num = ord(symbol)
                num += key
    
                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
    
                translated += chr(num)
            else:
                translated += symbol
        return translated
    
    mode = getMode()
    message = getMessage()
    key = getKey()
    
    print('Result:')
    print(getTranslatedMessage(mode, message, key))
    
acc = 'user/' + input('Login $ ')
type = getExtIndex(f'{acc}/info.ext', 1)
def check():
	if type.lower() == 'root':
		ps = input('Password $ ')
		password = getExtIndex(f'{acc}/info.ext', 2)
		if ps == password:
			pass
		else:
			print(tc.colored(f'Password {ps} is incorrect', 'red'))
			check()

check()
os.system('clear')
start()

class CMD(cmd.Cmd):
    intro = 'Simple command processor\nType "help" for a list of commands'
    type = getExtIndex(f'{acc}/info.ext', 1)
    if type.lower() == 'dev':
    	prompt = tc.colored("CMD ", 'green') + '- DEV $ '
    elif type.lower() == 'root':
    	prompt = tc.colored("CMD ", 'green') + '- ROOT $ '
    else:
        prompt = tc.colored("CMD ", 'green') + '$ '

    def do_echo(self, text):
        """echo [text]
        Echo [text] to terminal"""
        if text:
            print(text)
        else:
            print()

    def do_enc(self, any):
        """enc
        Open cipher tool"""
        cipher()

    def do_eval(self, problem):
        """eval [problem]
        Solve [problem] and echo result to terminal"""
        if problem:
            print(eval(problem))
        else:
            pass

    def do_cls(self, any):
        """cls
        Clear terminal screen"""
        os.system('clear')
        type = getExtIndex(f'{acc}/info.ext', 1)
        start()
        print('Simple command processor\nType "help" for a list of commands')
    
    def do_2048(self, any):
        """2048
        Open 2048 game"""
        os.system('py2048')
    
    def do_new(self, username):
    	"""new [username]
    	Make a new account"""
    	if type.lower() == 'root':
            if username:
                try:
                	os.mkdir('user/' + username)
                	file = open(f'user/{username}/info.ext', 'a')
                	file.write(f'{username}&dev')
                	file.close()
                except:
                    pass

    def do_app(self, file):
        """app [file]
        Open app named [file]"""
        os.system(f'python apps/{file}.py')
    
    def do_python(self, any):
        """python
        Open Python command interpreter"""
        os.system('python')

    def do_system(self, cmd):
        """system [cmd]
        Run Linux command [cmd]"""
        os.system(cmd)
    
    def do_user(self, any):
        """user
        Change user"""
        os.system('clear')
        os.system('python term.py')
        
    def do_zx(self, file):
        """zx [file]
        Run ZX script [file]"""
        os.system(f'python zx.py {acc}/{file}.zx')
    
    def do_info(self, tag):
        """info [tag]
        Echo info from catagory [tag] to terminal
        Tags: sys, cmd"""
        if tag:
        	if tag.lower() == "sys":
        		user = getExtIndex(f'{acc}/info.ext', 0)
        		type = getExtIndex(f'{acc}/info.ext', 1)
        		print(f'ⓘ System:\n- Name: {user}\n- Type: {type}')
        	elif tag.lower() == 'cmd':
        		print('ⓘ CMD:\n- Version: v1.0.0\n- Build: 787839')
        	else:
        		pass
    
    def do_whoami(self, any):
        """whoami
        Echo username to terminal"""
        user = getExtIndex(f'{acc}/info.ext', 0)
        print(user)
    
    def do_wait(self, time):
        """wait [time]
        Wait for [time] seconds"""
        sleep(int(time))

    def do_restart(self, any):
        """restart
        Restart CMD"""
        sleep(int(1))
        os.system('clear')
        os.system('python term.py')

    def postloop(self):
        print()

if __name__ == '__main__':
    CMD().cmdloop()
