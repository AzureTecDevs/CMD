# CMD
A simple python command interpreter made in Python 3.
# Required
+ CMD requires a couple modules:  
```pip install time```  
```pip install termcolor```  
```pip install cmd```  
```pip install py_cui_2048```  
+ A Linux system  
# Making your CMD account
When you run CMD, you are asked to enter your username. By default, there is one account named `root`. Login to this account with the password `12tte21k`. Once logged in, type `new [username]`. This will make a user called `[username]`. Then, type `restart` and login to your new account.  
![Commands](https://github.com/AzureTecDevs/CMD/blob/main/login.png)
# Using CMD
Once logged in to your account (see [Making your CMD account](#-making-your-cmd-account)), you have access to almost all CMD commands. To start, type `help`. You will see all of the commands available.  
![Commands](https://github.com/AzureTecDevs/CMD/blob/main/cmd.png)
## Commands
`echo [text]` : Echo `[text]` to the terminal  
`info [tag]` : Echo values of tag `[tag]` to the terminal  
`restart` : Restart CMD terminal  
`eval [problem]` : Evaluate `[problem]` and echo result to the terminal  
`wait [time]` : Wait for `[time]` seconds  
`2048` : Play 2048 in the terminal  
`user` : Change current user  
`whoami` : Echo current user's username to terminal  
`app [file]` : Run Python app `[file]`  
`python` : Open Python interpreter  
`cls` : Clear screen  
`new [username]` : Make an account named [username] (Only runs in `root` account)  
`zx [file]` : Run ZX script `[file]`
# Making ZX programs
## Setup your file
To make a ZX program, goto `/user/[username]` and make your file there. Example: `/user/azure/hello.zx`
## Programming
ZX programs are variable-based. This means `echo##hello world!` would be 
```
var##text##hello world!
echo##text
```
## Commands
`var##[name]##[val]` : set `[name]` to `[val]`  
`input##[var]` : set `[var]` to user's input  
`wait##[var]` : wait for `[var]` seconds  
`sys##[var]` : run Linux command `[val]`  
`exit` : Show `Press [ENTER] to quit` prompt (Use to keep app open)
## Examples
hello.zx:
```
# hello world program
# vars
var##txt##Hello World
var##wt##1
var##in##Nothing
# code
echo##txt
wait##wt
input##in##Text: 
echo##in
exit
```
