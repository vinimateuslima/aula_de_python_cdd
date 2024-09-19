opcao = 0
resultado = 0

n1 = float(input("Digite o primeiro número: "))

n2 = float(input("Digite o segundo número: "))

while opcao != 6:

    opcao = int(input("=-=-=-=-=-=-=-=-=-=-=-=-=-= \n"
                  "[1] para soma \n"
                  "[2] para subtração \n"
                  "[3] multiplicação \n"
                  "[4] divisão \n"
                  "[5] para digitar novo número \n"
                  "[6] para sair \n"
                  "=-=-=-=-=-=-=-=-=-=-=-=-=-= \n"
                  "Selecione a operação: "

                  ))
    if opcao == 1:
      resultado = n1 + n2
    elif opcao == 2:
        resultado = n1 - n2
    elif opcao == 3:
        resultado = n1 * n2
    elif opcao == 4:
        if n2 == 0:
            print("Não é possível realizar divisão por 0")
        else:
            resultado = n1 / n2

    elif opcao == 5:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

    print(f"O resultado da operação é: {resultado}")

print(f"Encerrando o programa...")

