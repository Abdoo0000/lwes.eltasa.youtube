import webbrowser
import os
os.system ("clear")
import time
print ("\033[0;31m |____________________|")
print ("\033[0;32m |                    |")
print ("\033[0;33m |   LWES             |")
print ("\033[0;34m |                    |")
print ("\033[0;35m |                    |")
print ("\033[0;37m |       ELTASA       |")
print ("\033[0;37m |                    |")
print ("\033[0;38m |                    |")
print ("\033[0;39m |                    |")
print ("\033[0;31m |             ELKBER |")
print ("\033[0;32m |    01283494514     |")
print ("\033[0;33m |____________________|")



url =  input("Enter the video url ")

refreshrate = input("Enter the refresh rate in seconds")

browserr = input("Enter your default browser name")


def letsdoit():
    os.system("TASKKILL /F /IM "+browserr+".exe")
    webbrowser.open(url)
    time.sleep(int(refreshrate))

views = input("How many views you want")
for i in range(int(views)+1):
    letsdoit()
