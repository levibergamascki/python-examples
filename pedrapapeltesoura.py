import random 

while True:
    escolhas = ["pedra", "papel", "tesoura"]
    computador = random.choice(escolhas)
    jogador = None
    contador_jogador = 0
    contador_computador = 0
    int_contador_computador = int(contador_computador) 
    int_contador_jogador = int(contador_jogador) 

    
    while jogador not in escolhas:
        jogador = input("pedra, papel ou tesoura? ").lower()

    if jogador == computador:
        print("computador: ", computador)
        print("jogador: ", jogador)
        print("empate")
        print("Placar: ", int_contador_jogador, " x ", int_contador_computador)

    elif jogador == "pedra":
        if computador == "papel":
            print("computador: ", computador)
            print("jogador: ", jogador)
            print("computador venceu!")
            int_contador_computador += 1
            print("Placar: ", int_contador_computador, " x ", int_contador_jogador)
        if computador == "tesoura":
            print("computador", computador)
            print("jogador", jogador)
            print("jogador venceu!")  
            int_contador_jogador += 1
            print("Placar: ", int_contador_computador, " x ", int_contador_jogador)   

    elif jogador == "papel":
        if computador == "pedra":
            print("computador: ", computador)
            print("jogador: ", jogador)
            print("jogador venceu!")
            int_contador_jogador += 1
            print("Placar: ", int_contador_computador, " x ", int_contador_jogador)   
        if computador == "tesoura":
            print("computador: ", computador)
            print("jogador: ", jogador)
            print("computador venceu!") 
            int_contador_computador += 1
            print("Placar: ", int_contador_computador, " x ", int_contador_jogador)   


    jogar_novamente = input("jogar novamente? (sim/não) ")

    if jogar_novamente != "sim":
        print("fim de jogo!")
        break

        
    
        


    