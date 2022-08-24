import random

def jogar():
    imprime_inicializacao()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicaliza_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    # enquanto
    while (not enforcou and not acertou):

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        # O jogador errando 6 vezes, "enforcou" se transforma em True e sai do loop, acabando o jogo.
        acertou = "" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_ganhador()

    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_inicializacao ():
    print("*********************************")
    print("Bem-vindo no jogo de Forca!******")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []  # guardando as palavras do arquivo em uma lista

    for linha in arquivo:  # for tem a função de percorrer, por isso pode-se chamar de laço.
        linha = linha.strip()  # A função strip() contida na classe string, elimina os espaços antes e depois da frase e caractéres especiais como "\n" que representa quebra de linha.
        palavras.append(linha)  # A função append tem a função de adicionar algo a uma lista, nesse caso, está adicionando o laço às palavras.
    arquivo.close()

    escolhendo_palavra = random.randrange(0,len(palavras))  # "len" devolve o tamanho da lista, é o que preciso pois o último item de um "range" é exclusivo.
    palavra_secreta = palavras[escolhendo_palavra].upper()
    return palavra_secreta

def inicaliza_letras_acertadas(palavra):
    return ["" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper() # A função strip() contida na classe string, elimina os espaços antes e depois da frase e caractéres especiais como "\n" que representa quebra de linha.
    return chute          #A função upper() contida na classe string, trata o valor do tipo STRING contida nas variáveis chute e letra como maiúsculas.

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0  # posição da letra (o nome "index" é uma variável, podendo ser mofificada)
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra  # "[index]" servindo como um contador para o laço ("for") dentro de palavra secreta!
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if (__name__ == "__main__"):
    jogar()
