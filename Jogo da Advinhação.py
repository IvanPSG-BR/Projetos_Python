from time import sleep
from random import randint


def dificuldade_do_jogo(nulo):
    pensando = nummaximo = 0
    niveldadificuldade = int(input('Selecione a sua dificuldade: '))

    while True:
        if niveldadificuldade >= 5 or niveldadificuldade <= 0:
            niveldadificuldade = int(input('Número incorreto. Digite uma opção válida: '))
        else:
            break

    if niveldadificuldade == 1:
        pensando, nummaximo = randint(1, 11), 10
    elif niveldadificuldade == 2:
        pensando, nummaximo = randint(1, 21), 20
    elif niveldadificuldade == 3:
        pensando, nummaximo = randint(1, 51), 50
    elif niveldadificuldade == 4:
        pensando, nummaximo = randint(1, 101), 100

    return [pensando, nummaximo, niveldadificuldade]


def jogo_da_adivinhacao():
    print(f'Ótimo, então vamos começar!')

    sleep(1.0)
    print("""Existem quatro dificuldades neste jogo:
[ 1 ] Fácil (número aleatório de 1 a 10);
[ 2 ] Médio (número aleatório de 1 a 20);
[ 3 ] Difícil (número aleatório de 1 a 50);
[ 4 ] Insano (número aleatório de 1 a 100);""")
    sleep(1.0)

    dificuldade = dificuldade_do_jogo('')

    sleep(1.0)
    print(f'Vou pensar em um número de 1 a {dificuldade[1]} e você vai tentar advinhar. Você terá '
          f'5 tentativas\nPensado...')
    sleep(3.0)

    usuario = int(input('Digite o número: '))
    tentativas = 4

    while usuario != dificuldade[0]:
        if usuario < dificuldade[0]:
            usuario = int(input('Tente um número mais alto: '))
            tentativas -= 1
        elif usuario > dificuldade[0]:
            usuario = int(input('Tente um número mais baixo: '))
            tentativas -= 1

        if usuario == dificuldade[0] and tentativas >= 1:
            print(f'Parabéns, você acertou faltando {tentativas}ª tentativas!')
            break
        elif tentativas == 0:
            print('Que pena, você perdeu! Acabou seu número de tentativas')
            break

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
        pergunta = input('Não entendi. Digite novamente S para sim ou N para não por favor: ').upper()
