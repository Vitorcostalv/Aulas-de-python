# Aula 10: Orientação a Objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando objetos
pessoa1 = Pessoa("Vitor", 20)
pessoa2 = Pessoa("Mari", 22)

# Chamando métodos
pessoa1.apresentar()
pessoa2.apresentar()
