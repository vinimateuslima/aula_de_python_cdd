numero = int(input("Digite um número: "))

contador = 0

while contador <= 10:
    resultado = numero * contador
    print(f"{contador} x {numero} = {resultado}")
    contador += 1
