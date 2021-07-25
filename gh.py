import hashlib

string= input("Digite o texto a ser gerador a hast : ")

resultado = hashlib.md5(string.encode('utf-8'))
print("O hast da string é: ", resultado.hexdigest())

menu = int(input(''''#### MENU - ESCOLHA O TIPO DE HAST ####
              1) MD5
              2) SHA1
              3) SHA256
              4) SHA3_256
              5) SHA512
              6) SHA3_512
              Digite o numero do hash a ser gerador: '''))
if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('A hast MD5 da String:', string, 'é:', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('A hast SHA1 da String:', string, 'é:', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('A hast SHA256 da String:', string, 'é:', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha3_256(string.encode('utf-8'))
    print('A hast SHA3_256 da String:', string, 'é:', resultado.hexdigest())
elif menu == 5:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('A hast SHA512 da String:', string, 'é:', resultado.hexdigest())

elif menu ==6:
    resultado = hashlib.sha3_512(string.encode('utf-8'))
    print('A hast SHA3_512 da String:', string, 'é:', resultado.hexdigest())
else:
    print("Escolhar uma opção de 1 a 7")