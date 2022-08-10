import os

os.system('mode con: cols=60 lines=50')
os.system('ping -t 192.168.1.201')
input("Press any key to continue...")

import os
#----------------------------------------------------------------------------------------
# command = "python --version" #command to be executed
# res = os.system(command)
# print("Returned Value: ", res)
# # Источник: https://pythononline.ru/osnovy/sistemnye-komandy-s-pomoschyu-python-os-system
#----------------------------------------------------------------------------------------

# import subprocess
#
# cmd = subprocess.Popen('cmd.exe /K mode con: cols=80 lines=300')
# cmd = subprocess.Popen('cmd.exe /K ping -t 192.168.1.201')
