# SSH-botnet
A python tool (automation) for automatically finding SSH servers on the network and adding them to the botnet for mass administration and control.

## Features

**Bot Collecting**

- [x] SSH Dictionary Attack

**Attack Method**

- [x] Command Execution

**File Upload**

- [x] File Uploading via SSH

**Bot Counting**

- [x] Bots Alive Function

## Requirements

**Python 3.9 (64-bit)**

At least 1 **bot** to start the **Attack**

## Installation

```
git clone https://github.com/tuananhkqtt/ssh-botnet
```


```
pip install -r requirements.txt --user
```
or
```
pip3 install -r requirements.txt --user
```

## Usage

Execute the **ssh.py** with **Python 3.9**: ( Don't use **sudo python ssh.py**, it won't work )
```
python ssh_botnet.py
```    
or
```
python3 ssh_botnet.py
```   

Then select the **option** that you want ( **Remember**, you need to have **some bots** before starting the attacks ):

```    

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
```

If you are **Attacking** just press **Ctrl+C** to stop it

## Disclaimer

This tool is only for testing and academic purposes and can only be used where strict consent has been given. **Do not use it for illegal purposes**. It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this tool and software in general.

## Author
* **Nguyen Minh Tai**       - [mtai83](https://github.com/mtai83)
* **Nguyen Tuan Anh**       - [tuananhkqtt](https://github.com/tuananhkqtt)
* **Nguyen Thuy Linh**      - [Rineee27](https://github.com/Rineee27)
* **Nguyen Viet Nhat Anh**  - [heliosmontana](https://github.com/heliosmontana)

## Inspirations

- [G0uth4m/SSH-botnet](https://github.com/G0uth4m/SSH-botnet)
- [kamiras/kamiras-ssh-botnet](https://github.com/kamiras/kamiras-ssh-botnet)
