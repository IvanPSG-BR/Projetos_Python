from time import sleep
from random import randint

def jogo_da_adivinhacao():
    print(f'Ótimo, então vamos começar!')

    sleep(1.0)
    print('Vou pensar em um número de 1 a 20 e você vai tentar advinhar. Você terá 5 tentativas \nPensado...')
    sleep(3.0)

    pensando = randint(1, 21)
    usuario = int(input('Digite o número: '))
    tentativas = 1

    while usuario != pensando and tentativas < 5:
        if usuario < pensando:
            usuario = int(input('Tente um número mais alto: '))
        elif usuario > pensando:
            usuario = int(input('Tente um número mais baixo: '))
        else:
            usuario = int(input('Número inválido. Tente novamente: '))
        tentativas += 1
    print(f'Parabéns, você acertou! na {tentativas}ª tentativa!' if tentativas < 5 else 'Que pena, acabaram '
                                                                                        'suas tentativas...')
    return 'Fim do Jogo'


pergunta = input('Vamos jogar um jogo de advinhação? [S/N]: ').upper()

while pergunta != 'S' or pergunta != 'N':
    while pergunta == 'S':
        print(jogo_da_adivinhacao())
        pergunta = input('Quer jogar novamente? [S/N]: ').upper()
        if pergunta == 'N':
            break
    if pergunta == 'N':
        print('Bom, que pena, então tchau!')
        break
    else:
        pergunta = input('Não entendi. Digite novamente por favor: ').upper()
