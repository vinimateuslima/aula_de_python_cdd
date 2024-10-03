alunos = int(input("Digite o número de alunos na sala: "))
soma = 0
contador = 0

while contador < alunos:
    nota = float(input(f"Digite a nota do {contador + 1} aluno: "))
    soma = soma + nota
    contador += 1

media = soma / alunos

print(f"A média da turma é: {media}")