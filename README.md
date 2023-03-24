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

  Command and Control Server (C2) and Payload Generator
  Author: Logan Goins

```

## Notes
This is a re-write of the software HeadHunter in python. HeadHunter was written entirely in C, but I've decided that python is a much better language for the software. Currently this version of HeadHunter is the equivalent of an older version of HeadHunter-C. This software currently receives and handles a reverse shell connection.
Although this software is technically a "lesser" version of the HeadHunter-C software, it's sizeably smaller and less complex than it's previous counterpart. This shows that by using python the development process can be simplified, and I can get this re-write operating with the same functionality as it's C counterpart in a smaller amount of time. (See https://github.com/Lionskey/HeadHunter-C)

Future features still include:

1. The ability to switch between infected and connected zombie connections
2. Some sort of daemonized process or thread that recursively accepts new machines to allow session switching
3. A more featureful payload (The current payload is just a simple and rather bland reverse shell connection). This would include beaconing, file transfer, persistance methods, and more.


I am not liable for any damage caused by this software. This software is for educational purposes only. This software is under the discretion of the end user.
