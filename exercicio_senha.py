cont = 0
while cont < 3:
    senha = input("Digite a senha: ")

    if (senha == "123"):
        print("Acesso liberado!")
        break

    print("Senha incorreta! tente novamente")
    cont += 1

    if (cont == 3):
        print("Acesso negado!")

