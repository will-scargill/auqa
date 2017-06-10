# import the colorama library
import os
from sys import path as syspath
syspath.append(os.path.join(os.path.dirname(__file__), "./lib/colorama"))

os.environ["TEST"] = "n" # Run Normally

import signal

import threading # to run each module simultaneously
from msvcrt import getch # to check for the esc key

from colorama import init, Fore, Back, Style # to change console colours
init() # init colorama

# show plant system ascii art text
print(Fore.GREEN + Style.BRIGHT + "   ___  __          __    ____         __          ")
print(Fore.GREEN + Style.BRIGHT + "  / _ \/ /__ ____  / /_  / __/_ _____ / /____ __ _ ")
print(Fore.GREEN + Style.BRIGHT + " / ___/ / _ `/ _ \/ __/ _\ \/ // (_-</ __/ -_)  ' \\")
print(Fore.GREEN + Style.BRIGHT + "/_/  /_/\_,_/_//_/\__/ /___/\_, /___/\__/\__/_/_/_/")
print(Fore.GREEN + Style.BRIGHT + "                           /___/                   ")

# reset colours
print(Style.RESET_ALL)

# import dashboard and sense modules
import dashboard
import sense

print(Fore.CYAN + Style.BRIGHT + " [i] Press `ESC` to quit.")

# make the dashboard and sense threads
sensethread = threading.Thread(target=sense.go)
dashboardthread = threading.Thread(target=dashboard.app.run)

# start the sense thread
print(Fore.CYAN + Style.BRIGHT + " [+] Starting Sense...")
sensethread.start()

# start the dashboard thread
print(Fore.CYAN + Style.BRIGHT + " [+] Starting Web Server...")
dashboardthread.start()

# keep checking for esc key
while True:
    key = ord(getch())
    if key == 27: # esc
        #quit
        print(Fore.RED + Style.BRIGHT + " [!] Stopping (user exit)...")
        print(Style.RESET_ALL)
        os.kill(os.getpid(), signal.SIGINT)
