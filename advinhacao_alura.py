import random 

def jogar_advinhacao():

    print('**********************************')
    print('    *** Jogo de advinhação! ***    ')
    print('**********************************')

    numero_secreto = random.randrange(1, 101)
    tentativas     = 0
    pontos         = 1000

    print('Qual o nível de dificuldade?')
    print("(1) Fácil: 20 rodadas (2) Médio: 10 rodadas (3) Difícil: 5 rodadas")

    nivel = int(input("Defina o nível:  "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel ==2):
        tentativas = 10
    else:
        tentativas = 5


    for rodada in range(1, tentativas +1):
        print("Rodada: {} de: {}".format(rodada, tentativas))

        chute_str = input('Digite o seu número: ')
        print('Você digitou ', chute_str)

        chute_int = int(chute_str)

        if (chute_int < 1 or chute_int > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = numero_secreto == chute_int
        menor   = numero_secreto > chute_int
        maior   = numero_secreto < chute_int

        if (acertou):
            print('Acertou!!!')
            print("Você fez {} pontos!".format(pontos))
            break
        else:
            if (menor):
                print('Errou! Seu número é menor que o número secreto')
                if (rodada == tentativas):
                    print('Acabaram suas tentativas. \nO número secreto era: {} \n Você fez {} pontos! \n.'
                          .format(numero_secreto, pontos))

            elif (maior):
                print('Errou! Seu número é maior que o número secreto')
                if (rodada == tentativas):
                    print('Acabaram suas tentativas. \nO número secreto era: {} \n Você fez {} pontos! \n.'
                          .format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos



    print('fim do jogo')
if(__name__=="__main__"):
    jogar_advinhacao()
