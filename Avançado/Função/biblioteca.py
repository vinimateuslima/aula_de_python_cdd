def piramide(numero):
    for i in range (numero+1):
        for x in range(1, i+1):
            print(x, end=" ")
        print()


def contarvogais(texto):
    cont=0
    t = len(texto)
    for x in range(t):
        if texto[x] in "aeiouAEIOU":
            cont += 1
    print(f"O texto possui {cont} vogais")


def somar(*numeros):
    resultado = 0
    for x in numeros:
        resultado += x

    print(resultado)

def novaLista(lista):
    nova_lista = []
    tam = len(lista)
    for x in range(tam):
        if lista[x] not in nova_lista:
            nova_lista.append(lista[x])

    print(nova_lista)

lista = [10, 12, 12, 31, 4, 4, 5, 31, 6, 7, 6, 8]

novaLista(lista)

def test_primo(numero):
    if numero == 1:
        return numero, "Não é primo"
    else:
        return numero, "É primo"

    for x in range(2, numero):
        if numero % x == 0:
            return numero, "Nâo é primo"
        else:
            return numero, "É primo"

