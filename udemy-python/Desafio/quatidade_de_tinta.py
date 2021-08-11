'''

Criar um progrma que calcula a quatidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer as seguintes informações : Redimento, altura e largura.
O programa deve mostar na tela a mensagem 'Você necessita de x lata de tinta

'''

redimento = float(input('Qual é o redimento da lata?: '))
altura_parede = float(input('Qual a Altura da parede?: '))
lagura_parede = float(input('Qual a lagura da parede?: '))

def resultando():
    area = altura_parede * lagura_parede
    total =  area / redimento
    print(f'Você precisar de {total} latas de tinta')
resultando()


