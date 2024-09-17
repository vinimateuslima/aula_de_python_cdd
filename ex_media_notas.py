n1 = 0
n2 = 0

n1 = int(input("Digite a primeira nota: "))

while n1 < 0 or n1 > 10:
    n1 = int(input("Nota inválida! Digite a primeira nota novamente: "))

n2 = int(input("Digite a segunda nota: "))

while n2 < 0 or n2 > 10:
    n2 = int(input("Nota inválida! Digite a segunda nota novamente: "))

media = n1 + n2 / 2

print(f"A média da nota é: {media}")