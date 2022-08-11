import os

os.system('mode con: cols=60 lines=50')
os.system('start cmd ping 192.168.1.200')
os.system('ping 192.168.1.201')
os.system('ping 192.168.1.202')
input("Press any key to continue...")

for ping in range(1,10):
   ip="127.0.0."+str(ping)
   os.system("ping -c 3 %s" % ip)

# typo error in import
#----------------------------------------------------------------------------
# import subprocess
#
# for ping in range(200,220):
#     address = "192.168.1." + str(ping)
#     # res = subprocess.call(['ping', '-c', '3', address])
#     res = subprocess.call(['ping', address])
#     if res == 0:
#         print("ping to", address, "OK")
#     elif res == 2:
#         print("no response from", address)
#     else:
#         print("ping to", address, "failed!")
#
# wait = input()
#-----------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# import os
# command = "python --version" #command to be executed
# res = os.system(command)
# print("Returned Value: ", res)
# # Источник: https://pythononline.ru/osnovy/sistemnye-komandy-s-pomoschyu-python-os-system
#----------------------------------------------------------------------------------------

# import subprocess
#
# cmd = subprocess.Popen('cmd.exe /K mode con: cols=80 lines=300')
# cmd = subprocess.Popen('cmd.exe /K ping -t 192.168.1.201')
