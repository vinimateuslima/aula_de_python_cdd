def criarArquivo(texto):
    with open("NomesTurmaC.txt", "a") as arquivo:
        arquivo.write(f"{texto}\n")
        print("Texto adicionado com sucesso!")


def imprimirArquivo():
    with open("NomesTurmaC.txt", "r") as arquivo2:
        print(arquivo2.read())

