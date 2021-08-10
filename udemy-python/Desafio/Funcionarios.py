# Desafio com 'Sets'

'''

Criar um progrma que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que tem carro em trabalham a noite
Lista2 = Funcionarios que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro
'''
funcionarios = ['Joao', 'Maria', 'Marcos', 'Pedro', 'Maria joao', 'Melissa', 'Bruno', 'Sophia', 'Alice' ]
turno_dia = ['Maria', 'Joao', 'Melissa', 'Alice']
turno_noite = ['Maria joao', 'Marcos', 'Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

# Lista 1
lista1 = set(tem_carro).intersection(turno_noite)

print(f'Tem Carro e Trabalha a Noite:  {lista1}')
# Lista2
lista2 = set(tem_carro).intersection(turno_dia)
print(f'Tem Carro mas Trabalha ao Dia!:  {lista2}')

#Lista 3
lista3 = set(funcionarios).difference(tem_carro)
print(f'Funcionarios que não tem carro{lista3}')


