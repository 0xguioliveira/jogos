def jogar():

    import random

    print ("*********************************")
    print("Bem-vindo no jogo de Adivinhação!")
    print ("*********************************")

    numero_secreto = random.randrange(1,101)
    print(numero_secreto)

    total_de_tentativas = 0
    pontos = 1000

    print ("Qual nível de dificuldade? ")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina um nível:"))
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}" . format(rodada, total_de_tentativas)) # "." para acessar o format

        chute_str = input("Digite o seu número entre 1 e 100:")
        print("Você digitou", chute_str)

        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        pontos_perdidos = abs(numero_secreto - chute)  # pontos perdidos na rodada, "abs" porque queremos o número absoluto/positivo
        pontos = pontos - pontos_perdidos  # subtraindo os pontos perdidos da pontuação atual.

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos} pontos.") #mesma coisa que .format já utilizado acima!!!

            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos} pontos.")

    print ("Fim do jogo.")



if (__name__=="__main__"):
    jogar()
