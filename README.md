# SSH-botnet
A python tool(automation) for automatically finding SSH servers on the network and adding them to the botnet for mass administration and control.

## Installation
```
$ pip install -r requirements.txt --user
```

## Usage
```
$ python ssh_botnet.py Wi-Fi

Author :	Nguyen Minh Tai
			Nguyen Tuan Anh
			Nguyen Thuy Linh
			Nguyen Viet Nhat Anh
GitHub : https://github.com/tuananhkqtt/ssh-botnet
	
		 _         _           _              _   
 ___ ___| |__     | |__   ___ | |_ _ __   ___| |_ 
/ __/ __| '_ \    | '_ \ / _ \| __| '_ \ / _ \ __|
\__ \__ \ | | |   | |_) | (_) | |_| | | |  __/ |_ 
|___/___/_| |_|___|_.__/ \___/ \__|_| |_|\___|\__|
             |_____|                              


[*] Scanning network for ssh servers ...
[+] Scan complete

Running ssh servers : 
Host : 192.168.56.105		port : 22
Host : 192.168.56.106		port : 22
Host : 192.168.56.107		port : 22

Continue adding bots to the botnet?[Y/n] y

ssh@botnet:~$ ls
[*] Output from 192.168.56.105
[+] ls
vulnerable

[*] Output from 192.168.56.106
[+] ls
vulnerable

[*] Output from 192.168.56.107
[+] ls
vulnerable

ssh@botnet:~$ uname -a
[*] Output from 192.168.56.105
[+] uname -a
Linux metasploitable 2.6.24-16-server #1 SMP Thu Apr 10 13:58:00 UTC 2008 i686 GNU/Linux

[*] Output from 192.168.56.106
[+] uname -a
Linux metasploitable 2.6.24-16-server #1 SMP Thu Apr 10 13:58:00 UTC 2008 i686 GNU/Linux

[*] Output from 192.168.56.107
[+] uname -a
Linux metasploitable 2.6.24-16-server #1 SMP Thu Apr 10 13:58:00 UTC 2008 i686 GNU/Linux

ssh@botnet:~$ id
[*] Output from 192.168.56.105
[+] id
uid=1000(msfadmin) gid=1000(msfadmin) groups=4(adm),20(dialout),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),107(fuse),111(lpadmin),112(admin),119(sambashare),1000(msfadmin)

[*] Output from 192.168.56.106
[+] id
uid=1000(msfadmin) gid=1000(msfadmin) groups=4(adm),20(dialout),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),107(fuse),111(lpadmin),112(admin),119(sambashare),1000(msfadmin)

[*] Output from 192.168.56.107
[+] id
uid=1000(msfadmin) gid=1000(msfadmin) groups=4(adm),20(dialout),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),107(fuse),111(lpadmin),112(admin),119(sambashare),1000(msfadmin)

ssh@botnet:~$ exit

[*] History of commands stored in logs.txt