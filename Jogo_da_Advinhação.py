from time import sleep
from random import randint


def dificuldade_do_jogo():
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
[ 1 ] Fácil (número aleatório de 1 a 10, onde você terá 4 tentativas para acertar);
[ 2 ] Médio (número aleatório de 1 a 20, onde você terá 5 tentativas para acertar);
[ 3 ] Difícil (número aleatório de 1 a 50, onde você terá 6 tentativas para acertar);
[ 4 ] Insano (número aleatório de 1 a 100, onde você terá 7 tentativas para acertar);""")

    sleep(1.0)
    dificuldade = dificuldade_do_jogo()
    sleep(1.0)

    listadetentativas = [3, 4, 5, 6]
    numschutados = []
    tentativas = 0
    for numdetentativas in range(0, len(listadetentativas)):
        if dificuldade[2] == (listadetentativas[numdetentativas]) - 2:
            tentativas = listadetentativas[numdetentativas]

    print(f'Vou pensar em um número de 1 a {dificuldade[1]} e você vai tentar advinhar. Você terá '
          f'{tentativas + 1} tentativas\nPensado...')
    sleep(3.0)
    usuario = int(input('Digite o número: '))

    while usuario != dificuldade[0]:
        sleep(0.5)
        while True:
            if usuario not in numschutados:
                numschutados.append(usuario)
                if 1 < usuario < dificuldade[0] and usuario < dificuldade[1]:
                    print(f'Você ainda tem {tentativas} chances')
                    sleep(1.0)
                    usuario = int(input('Tente um número mais alto: '))
                    tentativas -= 1
                    break
                elif 1 < usuario > dificuldade[0] and usuario < dificuldade[1]:
                    print(f'Você ainda tem {tentativas} chances')
                    sleep(1.0)
                    usuario = int(input('Tente um número mais baixo: '))
                    tentativas -= 1
                    break
                else:
                    usuario = int(input(f'Número inválido. Digite o número novamente, entre 1 e {dificuldade[1]}: '))
            else:
                usuario = int(input('Esse número já foi digitado. Por favor, digite outro: '))

        if usuario == dificuldade[0] and tentativas >= 1:
            print(f'Parabéns, você acertou faltando {tentativas} tentativas!')
            break
        elif tentativas == 0:
            print('Que pena, você perdeu! Acabou seu número de tentativas')
            break

    return 'Fim do Jogo'


def execucao_do_jogo():
    pergunta = input('Vamos jogar um jogo de advinhação? [S/N]: ').upper()

    while pergunta not in ['S', 'N', 'SIM', 'NÃO']:
        while pergunta == 'S' or pergunta == 'SIM':
            print(jogo_da_adivinhacao())
            pergunta = input('Quer jogar novamente? [S/N]: ').upper()
            if pergunta == 'N':
                break
        if pergunta == 'N' or pergunta == 'NÃO':
            print('Bom, que pena, então tchau!')
            sleep(1.5)
            break
        else:
            pergunta = input('Não entendi. Digite a opção novamente. S para sim ou N para não, por favor: ').upper()
