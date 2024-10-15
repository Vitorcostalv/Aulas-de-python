# Classe base
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass

# Classes derivadas
class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

# Usando polimorfismo
animais = [Cachorro("Rex"), Gato("Felix")]

for animal in animais:
    print(f"{animal.nome} diz: {animal.falar()}")

# Métodos especiais (__str__, __repr__)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

pessoa = Pessoa("Vitor", 20)
print(pessoa)
