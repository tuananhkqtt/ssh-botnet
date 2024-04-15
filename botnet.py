from bot import Bot
from datetime import datetime, date

class Botnet:

    def __init__(self):
        self.bots = []
        self.f = open('logs.txt', 'a')

    def addBot(self, host, user, password, port):
        print(self, host, user, password, port)
        if port != -1:
            bot = Bot(host, user, password, port)
            if  isinstance(bot.session, Exception):
                return bot.session
            elif not bot.session: 
                return False
            else:
                self.bots.append(bot) 
                return True
            
        else:
            print('[-] ssh server không chạy trên ' + host)
            return False

    def select_bot(self, index):
        i = 1
        for bot in self.bots:
            if i == index:
                return bot
            i += 1

    def command_single_bot(self, command, bot):
        self.f.write(" -> " + str(date.today().strftime("%B %d, %Y")) + " ( " + datetime.now().strftime("%H:%M:%S") + ' ) ' + '\n\n')
        result = bot.send_command(command)
        if isinstance(result, Exception):
            print(f"Error: {result}.")
        else:
            print(f'[*] Command sent IP:{bot.host} USER:{bot.user} PASS={bot.password}')
            print(result)
            self.f.write(str(result)+'\n')
        self.f.write(100*'-' + '\n')

    def command_all_bots(self, command):
        self.f.write(" -> " + str(date.today().strftime("%B %d, %Y")) + " ( " + datetime.now().strftime("%H:%M:%S") + ' ) ' + '\n\n')
        for bot in self.bots:
            result = bot.send_command(command)
            if isinstance(result, Exception):
                print(f"Error: {result}.")
            else:
                print(f'[*] Command sent IP:{bot.host} USER:{bot.user} PASS={bot.password}')
                print(result)
                self.f.write(str(result)+'\n')
            self.f.write(100*'-' + '\n')

    def up_file_single_bot(self, bot, localpath, remotepath):
        self.f.write(" -> " + str(date.today().strftime("%B %d, %Y")) + " ( " + datetime.now().strftime("%H:%M:%S") + ' ) ' + '\n\n')
        result = bot.upload_file(localpath, remotepath)
        if isinstance(result, Exception):
            print(f"Error: {result}.")
        else:
            print(f'[*] The file was sent successfully IP:{bot.host} USER:{bot.user} PASS={bot.password}')
            self.f.write(f'[*] The file {localpath} was sent successfully IP:{bot.host} USER:{bot.user} PASS={bot.password} and was located {remotepath}')
        self.f.write(100*'-' + '\n')

    def up_file_all_bots(self, localpath, remotepath):
        self.f.write(" -> " + str(date.today().strftime("%B %d, %Y")) + " ( " + datetime.now().strftime("%H:%M:%S") + ' ) ' + '\n\n')
        for bot in self.bots:
            result = bot.upload_file(localpath, remotepath)
            if isinstance(result, Exception):
                print(f"Error: {result}.")
            else:
                print(f'[*] The file was sent successfully IP:{bot.host} USER:{bot.user} PASS={bot.password}')
                self.f.write(f'[*] The file {localpath} was sent successfully IP:{bot.host} USER:{bot.user} PASS={bot.password} and was located {remotepath}')
                self.f.write(str(result)+'\n')
            self.f.write(100*'-' + '\n')
