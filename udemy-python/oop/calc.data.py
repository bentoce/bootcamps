from datetime import datetime
# criar a Classe
class clientes:
    def __init__(self, nome, sobrenome, data_nascimento, email, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
    def jls_extract_def(self):
        return ' '

    def nome_completo(self):
        return  self.nome + ' ' + self.sobrenome 
    def idade_clientes(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.data_nascimento)

    

# crair o objeto 
usuarios1 = clientes('Antonio', 'bento', 1985)
usuarios2 = clientes('Fran', 'sousa', 1981)

print(usuarios1.idade_clientes())
