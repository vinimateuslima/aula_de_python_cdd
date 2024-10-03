time1 = str(input("Digite o time 1: "))
time2 = str(input("Digite o time 2: "))
gol1 = int(input(f"Digite quantos gols o {time1} fez: "))
gol2 = int(input(f"Digite quantos gols o {time2} fez: "))

if gol1 > gol2:
    print("O ", time1, "ganhou o jogo!")
elif gol1 == gol2:
    print("Deu empate!")
else:
    print("O ", time2, "ganhou o jogo!")

