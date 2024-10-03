mes = int(input("Digite o número do mês: "))

resultado = ""

if (mes < 1 or mes > 12):
    print("Nùmero inválido")
else:

    if (mes == 1):
        resultado = "Janeiro"
    elif(mes == 2):
        resultado = "Fevereiro"
    elif (mes == 3):
        resultado = "Março"
    elif (mes == 4):
        resultado = "Abril"
    elif (mes == 5):
        resultado = "Maio"
    elif (mes == 6):
        resultado = "Junho"
    elif (mes == 7):
        resultado = "Julho"
    elif (mes == 8):
        resultado = "Agosto"
    elif (mes == 9):
        resultado = "Setembro"
    elif (mes == 10):
        resultado = "Outubro"
    elif (mes == 11):
        resultado = "Novembro"
    elif (mes == 12):
        resultado = "Dezembro"


    print(f"O mês selecionado é: {resultado}")

