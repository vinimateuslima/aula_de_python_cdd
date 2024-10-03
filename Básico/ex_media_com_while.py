contador = 0
soma = float(0)

while contador<10:
    nota = float(input(f"Digite a nota do {contador + 1} aluno: "))
    soma = soma + nota
    contador = contador + 1
media = soma / contador

print(f"A média da turma é: {media}")