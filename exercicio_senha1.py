cont = 2 # Contador inicia com 2 para ir decrementando as tentativas

senhaDoCartao = "123"

senha = input("Digite a senha: ")

# Enquanto a senha digitada for diferente da senha do cartão ele ficará no loop
while senha != senhaDoCartao:
    senha = input(f"Senha incorreta! Restam {cont} tentativas! \nDigite a senha novamente: ")

    # Se o contador for menor que 1 acabaram as tentativas
    if cont < 1:
       print("Acesso negado!")
       break

    cont -= 1

# Se não, ele libera o acesso
else:
    print("Acesso liberado!")

