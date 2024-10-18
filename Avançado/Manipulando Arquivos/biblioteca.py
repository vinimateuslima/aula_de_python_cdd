def criarArquivo(texto):
    with open("NomesTurmaC.txt", "a") as arquivo:
        arquivo.write(f"{texto}\n")
        print("Texto adicionado com sucesso!")


def imprimirArquivo():
    with open("NomesTurmaC.txt", "r") as arquivo2:
        print(arquivo2.read())


def pesquisar(texto):
    with open("NomesTurmaC.txt", "r") as pesq:
        for x in pesq:
            print("passou ", x)
            if texto in x:
                print(f"O texto {texto} foi encontrado na lista")
                break
        else:
            print("Nenhum texto foi encotrado")



