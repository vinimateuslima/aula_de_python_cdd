usuario = [""]*5

tam = len(usuario)

senha = [""]*tam

opcao = 0

opcao = int(input(" 1 - Cadastro \n"
          " 2 - Mostrar \n"
          " 3 - Login \n"
          " 4 - Sair \n"
          " 5 - Deletar contas \n "
          "Selecione uma opção: "))
print()
while opcao != 4:


    if opcao == 1:
        for i in range(tam):
            if usuario[i] == "":
                usuarioNovo = input("Digite um usuário: ")
                if usuarioNovo not in usuario:
                    usuario[i] = usuarioNovo
                    senha[i] = input("Digite a senha do usuário: ")
                    print("Cadastro realizado com sucesso!")
                    break
                else:
                    print("Usuário ja existe!")
                    break
        else:
            print()
            print("Limite de usuários excedido!")

    if opcao == 2:
        print("Lista de usuários cadastrados")
        print(usuario)
        print(senha)

    if opcao == 3:
        print("-=-=-=-=-=-=-=-= Realizar Login =-=-=-=-=-=-=-=-=-")

        usuarioDigitado = input("Digite o usuário: ")

        for i in range(tam):

            if usuarioDigitado not in usuario:
                print("Usuário não encontrado!")
                break

            if  usuarioDigitado == usuario[i] :
                tentativa = 2

                while tentativa >= 0:

                    senhaDigitada = input("Digite a senha: ")

                    if senha[i] == senhaDigitada:
                        print(f"Login realizado com sucesso! Bem vindo(a) {usuario[i]}")
                        break
                    else:
                        print(f"Senha incorreta! Você possui {tentativa} tentativas.")
                        tentativa -= 1
                else:
                    print("Número de tentativas excedidas!")

    if opcao == 5:
            usuario = [""] * 5
            senha = [""] * 5
            print("Usuários removidos com sucesso!")








    print()
    print("Deseja realizar outra operação?")
    opcao = int(input(" 1 - Cadastro \n"
              " 2 - Mostrar \n"
              " 3 - Login \n"
              " 4 - Sair \n"
              " 5 - Deletar contas \n "
              "Selecione uma opção: "))
else:
    print("Saindo do programa...")
