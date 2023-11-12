import cmd
import os
import sys
import termcolor as tc
from ext import *
from time import sleep

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
    
    def do_user(self, any):
        """user
        Change user"""
        os.system('clear')
        os.system('python term.py')

    
    def do_info(self, tag):
        """info [tag]
        Echo info from catagory [tag] to terminal
        Tags: sys, cmd"""
        if tag:
        	if tag.lower() == "sys":
        		user = getExtIndex(f'{acc}/info.ext', 0)
        		type = getExtIndex(f'{acc}/info.ext', 1)
        		print(f'System:\n- Name: {user}\n- Type: {type}')
        	elif tag.lower() == 'cmd':
        		print('CMD:\n- Version: v1.0.0\n- Build: 74928')
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