from biblioteca import *

print(" 1 - Gravar \n "
      "2 - Mostrar \n "
      "3 - Pesquisar \n"
      " 4 - Sair \n")
opcao = int(input("Digite a opção: "))

while True:

    match opcao:
        case 1:
            texto = input("Digite um texto: ")
            criarArquivo(texto)
        case 2:
            imprimirArquivo()
        case 3:
            pass
        case 4:
            print("Encerrando o programa...")
            break

    print(" 1 - Gravar \n "
          "2 - Mostrar \n "
          "3 - Pesquisar \n"
          " 4 - Sair \n")
    opcao = int(input("Deseja realizar outra operação? "))