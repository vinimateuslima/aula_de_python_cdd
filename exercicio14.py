numero = int(input("Digite um número: "))

for x in range(1, 10, 1):
    if x % 2 != 0:
        print(f"{x}", end=" ")