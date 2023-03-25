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

  Command and Control Server (C2) for Unix like operating systems
  Author: Logan Goins

```

## Notes
This software receives and handles a reverse shell connection, giving the operator of the (C&C) server access to the infected zombie device. 

Future features include:

1. The ability to switch between infected and connected zombie connections
2. A more featureful payload (The current payload is just a simple and rather bland reverse shell connection). This would include beaconing, file transfer, persistance methods, and more. As well as a dedicated windows payload, as the currently payload is untested on Windows as the server is intended to be for Unix like operating systems
3. Encryption for server/payload communcation



I am not liable for any damage caused by this software. This software is for educational purposes only. This software is under the discretion of the end user.
