numero = int(input("Digite um número: "))

for x in range(numero + 1):
    for i in range(0, x):
        print(i, end=" ")
    print()
