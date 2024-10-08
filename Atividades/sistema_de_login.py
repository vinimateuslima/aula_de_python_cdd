usuario = [0]*5

tam = len(usuario)

senha = [""]*tam

opcao = 0

opcao = int(input("1 - Cadastro \n"
          " 2 - Mostrar \n"
          " 3 - Login \n"
          " 4 - Sair \n "
          "Selecione uma opção: "))

while opcao != 4:


    if opcao == 1:
        for i in range(10):
            print(i)
            if i == 5:
                break

    opcao = int(input("1 - Cadastro \n"
              " 2 - Mostrar \n"
              " 3 - Login \n"
              " 4 - Sair \n "
              "Selecione uma opção: "))
