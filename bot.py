import paramiko

class Bot:
    
    def __init__(self, host, user, password, port):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.session = self.connect()

    def connect(self):
        try:
            bot = paramiko.SSHClient()
            bot.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            bot.connect(hostname=self.host, port=self.port, username=self.user, password=self.password)
            return bot
        except paramiko.ssh_exception.AuthenticationException:
            print(f'[*] Authentication Failed IP:{self.host} USER:{self.user} PASS={self.password}')
            return
        except paramiko.SSHException as e:
            print(f'[*] Device Failed Executing the Command IP:{self.host} USER:{self.user} PASS={self.password}')
            return e
        except Exception as e:
            return e

    def send_command(self, cmd):
        try:
            stdin, stdout, stderr = self.session.exec_command(cmd)
            if 'nohup' in cmd:
                return ''
            return stdout.read().decode()
        except Exception as e:
            return e
        
    def upload_file(self, localpath, remotepath):
        self.sftp = self.session.open_sftp()
        try:
            self.sftp.put(localpath, remotepath)
        except Exception as e:
            return e
