arrayNome = [""]*5
arraySenha = [""]*5

tam = len(arrayNome)

for x in range(tam):
    arrayNome[x] = input("Digite o nome de usuário: ")
    arraySenha[x] = input("Digite a senha: ")

for i in range(tam):
    print(f"Posição: {i} Nome: {arrayNome[i]} Senha: {arraySenha[i]} \n")

