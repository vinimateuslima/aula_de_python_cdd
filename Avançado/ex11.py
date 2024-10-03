numeros = [""]*10

tam = len(numeros)

contador = 0

for i in range(tam):
    numeros[i] = int(input("Digite um número: "))

maisUmNumero = int(input("Agora digite mais um número: "))

for x in range(tam):
    if (numeros[x] == maisUmNumero):
        contador += 1

print(f"O número {maisUmNumero} aparece {contador} vezes no array")