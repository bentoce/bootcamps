import os # Import o módulo ou biblioteca os (integra os programas e recurso do S.O
import time

print ("-" * 100) # imprimido 100 vezes
ip_ou_host = input("Digite  o IP ou host a ser verificado?: ")
#criado uma variavel que vai receber do usuariso up ip

os.system('ping -c 2 {}'.format(ip_ou_host))
## chamando system da biblioteca os - comando ping
# -c -num pacotes que serão - 60 vezea

print("-" * 100)