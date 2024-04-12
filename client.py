# from pexpect import pxssh

# class Client:
	
# 	def __init__(self, host, user, password, por):
# 		self.host = host
# 		self.user = user
# 		self.password = password
# 		self.por  = por
# 		self.session = self.connect()

# 	def connect(self):
# 		try:
# 			s = pxssh.pxssh()
# 			s.login(self.host, self.user, self.password, port=self.por)
# 			return s
# 		except Exception as e:
# 			print(e)
# 			print('[-] Error Connecting')
# 			exit()

# 	def send_command(self, cmd):
# 		self.session.sendline(cmd)
# 		self.session.prompt()
# 		return self.session.before

import paramiko
import os

class Client:
    
    def __init__(self, host, user, password, port):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.session = self.connect()
        # self.__sftp = self.session.open_sftp()
        # self.__current_dir = self.__sftp.normalize('.')

    def connect(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self.host, port=self.port, username=self.user, password=self.password)
            return client
        except Exception as e:
            print(e)
            print('[-] Lỗi kết nối ', self.host)
            return e
            # exit()

    def send_command(self, cmd):
        try:
            stdin, stdout, stderr = self.session.exec_command(cmd)
            output = stdout.read().decode()
            return output
        except Exception as e:
            print(e)
            return None
        
    def uploadFile(self, localFilePath):
        self.__sftp = self.session.open_sftp()
        self.__current_dir = self.__sftp.normalize('.')
        try:
            fileName = os.path.basename(localFilePath)
            remoteFilePath = f'{self.__current_dir}/{fileName}'
            self.__sftp.put(localFilePath, remoteFilePath)
            print(f'\t\tUploaded {fileName} success!!!')
        except IOError:
            print(f'\t\tCommand invalid! Please try again...!')