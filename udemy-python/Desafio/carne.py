# Desafio com If, Elif, Else

'''
Criar um programa que depedendo da temperatura (em celsius) do steak
ele retorna o ponto de cozimento em portugues. O usuria deverá fornecer a temperatrura


Temperaturas - Cozimento
120ºF ou 48ºC - Rare ( Selada)
130Fº ou 54ºC - Medium rare ( Ao ponto para o mal)
140º ou 60ºC - medium ( Ao ponto)
150ºF ou 65ºC - Medium well ( Ao ponto para o bem)
160ºF ao 71ºC - Well done (Bem passada)
'''
tem_cel = int(input('Qual a temperatura da carne?: '))

if tem_cel in range(0, 47):
    print('Cozinha po mais algum minutos !')
elif  tem_cel in range(48, 53):
    print('Ao ponto para o mal')
elif  tem_cel in range(54, 59):
    print('Ao ponto')
elif  tem_cel in range(60, 64):
    print('Ao ponto para o bem')
elif  tem_cel in range(65, 70):
    print('Bem passada')
elif tem_cel in range(71,201):
    print('Quimanda!')
else:
    print('Digite uma valor validor de 0 a 200!')



