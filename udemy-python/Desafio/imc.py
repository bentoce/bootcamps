# Calculo de IMC - Ímdice de Massa Corporal

altura= float(input('Qual é a sua Altura em cm ?:'))
peso = float(input('Qual é o seu peso em kg ? :'))

IMC = peso / (altura/100)**2
print(IMC)

if IMC < 18.5:
    print('Magreza')

elif IMC in float(range(18.5, 24.9)):
    print('NORMAL')
elif IMC in float(range(25.0, 29.9)):
    print('SOBREPESO')
elif IMC in float(range(30.0, 39.9)):
    print('OBSIDADE')
elif IMC > float(40.0):
    print('OBESIDADE GRAVE')
else:
    print('Digite o Valor validor para calcular IMC ?:')





# MENOR QUE 18,5 MAGREZA
# ENTRE 18,5 E 24,9 NORMAL
# ENTRE 25,0 E 29,9 SOBREPESO
# ENTRE 30,0 E 39,9 OBSIDADE
# MAIOR QUE 40,0    OBESIDADE GRAVE


