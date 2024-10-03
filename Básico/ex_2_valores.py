opcao = 1

while opcao == 1:

    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    contador = 0

    while valor2 <= 0:
          valor2 = int(input("Valor inválido Digite o segundo valor que seja diferente de 0: "))

    resultado = valor1 / valor2
    print(f"O resultado da divisão de {valor1} por {valor2} é: {resultado}")

    opcao = int(input("Deseja continuar \n"
                      "1 para sim\n"
                      "2 pare não: "))

