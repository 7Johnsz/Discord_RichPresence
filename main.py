import time
import os

from pypresence import Presence
from colorama import Fore, Style

# Application

client_id = "Your Application ID"

# Creating a function that, when activated with some parameter, runs in presence with Application ID

RPC = Presence(client_id)

# Just a banner and warn start xD

def start():
    os.system('cls')

    banner = (f""" 
    {Fore.BLUE}{Style.BRIGHT}

     ╦┌─┐┬ ┬┌┐┌┌─┐┌─┐ │ 
     ║│ │├─┤│││└─┐┌─┘ │ https://github.com/7Johnsz
    ╚╝└─┘┴ ┴┘└┘└─┘└─┘ │  

    {Fore.RESET}{Style.RESET_ALL}
    """)

    print(banner)
    print(Fore.GREEN + "[-] " + Fore.RESET + Style.BRIGHT + "Starting RichPresence" + Style.RESET_ALL)

# Creating a function to try to connect with your application

def connectRpc():
    RPC.connect()

# Attempt to establish connection

def connectLoop(conn=0):
    if conn > 10:
        return

    try:
        connectRpc()

    except Exception as e:
        print(Fore.RED + "[!]" + Fore.RESET + Style.BRIGHT,e,Style.RESET_ALL)

        time.sleep(2)
        exit()

    else:
        update()

# Here you can customize your rich presence

def update():
    print(Fore.GREEN + "[-] " + Fore.RESET + Style.BRIGHT + "Rich Presence is working" + Style.RESET_ALL)

    try:
        while True:
            RPC.update(buttons=[{"label":"example", "url":"https://bit.ly/3nzNusS"}])

            time.sleep(15)


    except KeyboardInterrupt:
        print("\n" + Fore.RED + "[!] " + Fore.RESET + Style.BRIGHT + "Keyboard Interrupt" + Style.RESET_ALL)
        time.sleep(2)
        RPC.clear()

# Calling the start function and starting the script

start()
connectLoop()