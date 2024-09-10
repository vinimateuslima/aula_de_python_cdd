combustivel = str(input("Informa o tipo de combustível G para Gasolina E para Etanol: "))
litros = float(input("Digite quantos litros de combustível: "))

valorTotal = int(0)

if combustivel == "G":
    valorTotal = litros*5.80
    print(f"O valor total é: R${valorTotal} ")
elif combustivel == "E":
    valorTotal = litros * 4.90
    print(f"O valor total é: R${valorTotal} ")
else:
    print("Opção inválida!")

