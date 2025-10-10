#!/usr/bin/env/python3
# This Python file uses the following encoding:utf-8

# ===== #
#   
# ▀█████████▄     ▄████████         Websites: HackingPassion.com
#   ███    ███   ███    ███         Author: Jolanda de Koff aka Bulls Eye
#   ███    ███   ███    █▀          GitHub: https://github.com/BullsEye0
#  ▄███▄▄▄██▀   ▄███▄▄▄             linkedin: https://www.linkedin.com/in/jolandadekoff
# ▀▀███▀▀▀██▄  ▀▀███▀▀▀             Facebook Group: https://www.facebook.com/groups/hack.passion/
#   ███    ██▄   ███    █▄          Facebook: https://www.facebook.com/ethical.hack.group
#   ███    ███   ███    ███         Twitter: https://twitter.com/bulls__eye
# ▄█████████▀    ██████████         LBRY: https://lbry.tv/$/invite/@hackingpassion:9
#                                   Patreon: https://www.patreon.com/jolandadekoff
#          Bulls Eye..!
# ===== #

# DNS Changer Eye Created Oktober 2023

# Copyright (c) 2023 Jolanda de Koff. HackingPassion.com

########################################################################

# A notice to all nerds and n00bs...
# If you will copy the developer's work it will not make you a hacker..!
# Respect all developers, we doing this because it's fun...

########################################################################

import os
import random
import time

print(""" \033[1;34m
                                                                                             
ooo.   o    o .oPYo.   .oPYo. 8                                         .oPYo.               
8  `8. 8b   8 8        8    8 8                                         8.                   
8   `8 8`b  8 `Yooo.   8      8oPYo. .oPYo. odYo. .oPYo. .oPYo. oPYo.   `boo   o    o .oPYo. 
8    8 8 `b 8     `8   8      8    8 .oooo8 8' `8 8    8 8oooo8 8  `'   .P     8    8 8oooo8 
8   .P 8  `b8      8   8    8 8    8 8    8 8   8 8    8 8.     8       8      8    8 8.     
8ooo'  8   `8 `YooP'   `YooP' 8    8 `YooP8 8   8 `YooP8 `Yooo' 8       `YooP' `YooP8 `Yooo' 
.....::..:::..:.....::::.....:..:::..:.....:..::..:....8 :.....:..:::::::.....::....8 :.....:
::::::::::::::::::::::::::::::::::::::::::::::::::::ooP'.::::::::::::::::::::::::ooP'.:::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::...::::::::::::::::::::::::::...:::::::::

            \033[1;m
        \033[34mDNS Changer Eye \033[0m
        \033[34mAuthor: Jolanda de Koff aka Bulls Eye \033[0m
        \033[34mGithub:  https://github.com/BullsEye0 \033[0m
        \033[34mWebsite: https://hackingpassion.com \033[0m
        \033[34mPatreon: https://www.patreon.com/jolandadekoff \033[0m

              Hi there, Shall we play a game..? 😃 
              
              """)

dns_servers = [
    "1.1.1.1", "1.0.0.1", 
    "9.9.9.9", "149.112.112.112", 
    "208.67.222.222", "208.67.220.220", 
    "64.6.64.6", "64.6.65.6", 
    "91.239.100.100", "89.233.43.71", 
    "185.228.168.9", "185.228.169.9", 
    "77.88.8.8", "77.88.8.1", 
    "176.103.130.130", "176.103.130.131", 
    "156.154.70.1", "156.154.71.1", 
    "199.85.126.10", "199.85.127.10", 
    "81.218.119.11", "209.88.198.133", 
    "195.46.39.39", "195.46.39.40", 
    "205.210.42.205", "64.68.200.200", 
    "216.146.35.35", "216.146.36.36", 
    "37.235.1.174", "37.235.1.177", 
    "198.101.242.72", "23.253.163.53", 
    "77.88.8.7", "77.88.8.3", 
    "77.88.8.88", "77.88.8.2", 
    "85.214.20.141", "81.3.27.54", 
    "91.239.100.100", "89.233.43.71", 
    "74.82.42.42", "109.69.8.51", 
    "84.200.69.80", "84.200.70.40", 
    "8.26.56.26", "8.20.247.20", 
    "208.76.50.50", "208.76.51.51", 
    "216.87.84.211", "45.33.81.76", 
    "192.169.69.9", "192.169.69.10",
    "185.121.177.177", "185.121.177.53",
    "195.10.46.179", "212.82.225.7",
    "194.168.4.100", "194.168.8.100",
    "203.122.222.6", "203.122.223.6",
    "209.254.0.3", "209.244.0.4",
    "109.88.203.3", "62.197.111.140",
    "194.38.104.56", "194.38.105.56",
    "203.118.141.194", "203.118.141.195",
    "203.79.252.114", "203.79.252.115"
]

def change_dns():
    while True:
        new_dns1, new_dns2 = random.sample(dns_servers, 2)
        os.system(f"echo 'nameserver {new_dns1}\nnameserver {new_dns2}' | sudo tee /etc/resolv.conf")
        time.sleep(300)  # Change DNS every 5 minutes

if __name__ == "__main__":
    change_dns()
