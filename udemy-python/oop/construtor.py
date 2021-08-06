# criar a Classe
class clientes:
    def __init__(self, nome, sobrenome, data_nascimento, email, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = email
        self.endereco = endereco

# crair o objeto 
usuarios1 = clientes('Antonio', 'bento', '22/04/1985', 'bento.ti@outlook.com', 'Rua azavedo bolão 1271')
usuarios2 = clientes('Fran', 'sousa', '02/06/1985', 'bento.ti@outlook.com', 'Rua azavedo bolao 1271')

print(usuarios1.nome)
print(usuarios2.nome)
