
n1 = int(input("Insira a primeira nota: "))
n2 = int(input("Insira a segunda nota: "))
n3 = int(input("Insira a terceira nota: "))
media = int((n1 + n2 + n3) / 3)

if (n1 < 0 or n1 > 10) and (n2 < 0 or n2 > 10) and (n3 < 0 or n3 > 10):
    print("Número inválido!")
else:
    if media >= 7:
        print("Aprovado!")
    elif media >= 4:
        print("Recuperaçãp!")
    else:
        print("Reprovado!")