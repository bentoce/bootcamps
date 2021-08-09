import os
import time

with open('hosts.txt') as file:
   dump = file.read()
   dump = dump.splitlines()

for ip in dump:
 print('Verificando o ip:', ip)
print('-'* 60)
os.system('ping -c 5 {}'.format(ip))
print('-'* 100)
time.sleep(5)

