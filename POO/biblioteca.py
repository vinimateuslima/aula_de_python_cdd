from operator import truediv

class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.andando = False
        self.comendo = False
        self.dormindo = False

    def comer(self):
        if self.comendo == True:
            print("Ja estou comendo bobão")
        elif self.andando == True:
            print("Não posso comer andando, sou burro")
        elif self.dormindo == True:
            print("ZzzzZzzzZzzzz")
        else:
            print("Vou começar a comer")
            self.comendo = True


    def andar(self):

        if self.andando == False:
            print(f"{self.nome} Está andando")
            self.andando = True
        else:
            print("Ja estou andando")


    def pararDeAndar(self):
       if self.andando == True:
           print("Parei de andar")
           self.andando = False
       else:
           print("Ja estou parado")



    def dormir(self):
        print(f"{self.nome} foi dormir")
        self.dormindo = True


class Animal:
    def __init__(self, nome, cor, comendo=False):
        self.nome = nome
        self.cor = cor
        self.comendo = comendo

        def comer (self):
            print("Estou comendo")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar (self):
        print(f" O {self.nome} foi miando...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f" O {self.nome} está latindo...")

    def comer(self):
        print(f" O cachorro {self.nome} foi comer...")



