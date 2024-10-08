usuario = [""]*5

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
        for x in range(tam):

            usuario[x] = input("Digite o nome de usuário: ")

            if usuario[x] == '123':
                print("Nome de usuário '123' não é permitido.")
                break  # Sai do loop se o nome for '123'

            print("Usuário cadastrado com sucesso!")
            break  # Sai do loop após cadastrar um usuário

        else:
            print("Limite de usuários atingido")


print("Deseja realizar outra operação? ")

opcao = int(input("1 - Cadastro \n"
          " 2 - Mostrar \n"
          " 3 - Login \n"
          " 4 - Sair \n "
          "Selecione uma opção: "))
