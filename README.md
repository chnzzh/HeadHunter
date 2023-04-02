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

## Dependencies
rsa (pip install rsa)

## Notes
HeadHunter is a cross platform, session based command and control (C2) server to handle reverse shell connections from infected zombie devices. The operator of HeadHunter has the ability to switch between multiple infected devices through the interactive shell interface. All communications between HeadHunter and the custom payload are encrypted in NIST recommended RSA 2048 bit asymmetric encryption. 

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

The HeadHunter payload is located in the "src" directory. Change the connect back address in the source code to the address of your C2 server. When your target runs a Windows compiled executable of the payload (or just the payload itself) it will connect back to the C2 server. This will give the operator control of the infected device.

## Extra Notes

For Windows binaries/executables I recommend auto-py-to-exe or pyinstaller to convert the payload to an executable. Make sure to change the attacker connect back address in the payload code before compilation. Also note that cross-compilation is impossible. Unfortunately to compile for Windows you will need a Windows installation of your own. I'm still currently looking for a solution on cross-compilation, but pyinstaller does not support it. 
