from operator import truediv


class Pessoa:
    def __init__(self, nome, peso, idade, andando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.andando = andando

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

    def comer(self):
        print(f"{self.nome} foi comer")

    def dormir(self):
        print(f"{self.nome} foi dormir")

