# import the colorama library
import os
from sys import path as syspath
syspath.append(os.path.join(os.path.dirname(__file__), "./lib/colorama"))

from colorama import init, Fore, Back, Style # to change console colours
init() # init colorama

os.environ["TEST"] = "n" # Run Normally

try:
    from sense_hat import SenseHat
except ModuleNotFoundError:
    print(Fore.RED + Style.BRIGHT + " [!] The Sense Hat module is not installed. Starting in testing mode...")
    os.environ["TEST"] = "y" # Run in Test Mode

import signal

import threading # to run each module simultaneously

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

# make the dashboard and sense threads
sensethread = threading.Thread(target=sense.go)
dashboardthread = threading.Thread(target=dashboard.app.run)

# start the sense thread
print(Fore.CYAN + Style.BRIGHT + " [+] Starting Sense...")
sensethread.start()

# start the dashboard thread
print(Fore.CYAN + Style.BRIGHT + " [+] Starting Web Server...")
dashboardthread.start()

# run forever
while True:
    pass
