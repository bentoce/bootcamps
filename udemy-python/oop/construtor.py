# criar a Classe
class clientes:
    def __init__(self, nome, sobrenome, data_nascimento, email, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = email
        self.endereco = endereco
    def jls_extract_def(self):
        return ' '

    def nome_completo(self):
        return  self.nome + ' ' + self.sobrenome +self.jls_extract_def() + self.email + ' ' + self.endereco


# crair o objeto 
usuarios1 = clientes('Antonio', 'bento', '27/07/1982', 'bento.ti@outlook.com', 'Rua azavedo bolão 1271')
usuarios2 = clientes('Fran', 'sousa', '02/06/1985', 'fransouza@gmail.com', 'Rua azavedo bolao 1271')

print(usuarios1.nome_completo())
print(usuarios2.nome_completo())
