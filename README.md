# HeadHunter

```
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

```

## Notes
This software receives and handles a reverse shell connection, giving the operator of the (C&C) server access to the infected zombie device. 

Future features include:


1. A more featureful payload (The current payload is just a simple and rather bland reverse shell connection). This would include beaconing, file transfer, persistance methods, and more. As well as a dedicated windows payload, as the currently payload is untested on Windows as the server is intended to be for GNU/Linux based operating systems
2. RSA 2048 bit encryption for communication between payload and server
3. The ability to command multiple connected sessions



I am not liable for any damage caused by this software. This software is for educational purposes only. This software is under the discretion of the end user.

## Use Guide

1. Clone the HeadHunter source
```
git clone https://github.com/Lionskey/HeadHunter
```

2. Change into source directory
```
cd HeadHunter
```

3. Execute install script
```
sudo ./install.sh
```

4. Run HeadHunter interactive shell
```
headhunter
```

For Windows binaries/executables I recommend auto-py-to-exe or pyinstaller to convert the payload to an executable. Make sure to change the attacker connect back address in the payload before compilation. 
