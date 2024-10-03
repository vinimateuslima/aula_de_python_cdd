resultado = int()

for x in range(10):
    numero = int(input("Digite um número: "))

    if numero % 2 != 0:
        resultado = resultado + numero

print(f"O resultado da soma de todos os números impares é: {resultado}")