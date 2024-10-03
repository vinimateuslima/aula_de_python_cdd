numeros = [""]*5

tam = len(numeros)

numerosPares = [""]*tam


soma = 0
contador = 0

for i in range(tam):
    numeros[i] = int(input("Digite um número: "))

menor = numeros[0]

for x in range(tam):
    if numeros[x] % 2 == 0:
        numerosPares[x] = numeros[x]

    if numeros[x] < menor:
        menor = numeros[x]

    soma += numeros[x]

media = soma / tam

for z in range(tam):
    if (numeros[z] > media):
        contador += 1

print(f"Os números pares existentes são {numerosPares}")
print(f"O menor valor é: {menor}")
print(f"Existem {contador} números maiores que o valor da média")
