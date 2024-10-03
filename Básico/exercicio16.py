alunos = int(input("Digite o número de alunos na sala: "))
soma = float()

for x in range(0, alunos, 1):
    nota = float(input(f"Digite a nota do {x + 1} aluno: "))
    soma = soma + nota

media = soma / alunos

print(f"A média da turma é: {media}")