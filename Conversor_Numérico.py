from time import sleep

print('=' * 36)
print('    CONVERSOR DE BASES NUMÉRICAS')


def conversor_numerico():

    while True:
        sleep(2.0)
        print('=' * 36)
        print('''Digite:
10 para decimal;
2 para binário;
8 para octal;
16 para hexadecimal;
0 para sair do programa''')
        sleep(2.0)
        print('=' * 36)

        baseparaconverter = int(input('Base numérica a ser convertida (para sair do programa digite 0): '))
        if baseparaconverter == 0:
            break
        numconvertido = int(input('Base para qual você quer converter: '))

        print('=' * 36)
        conversao = 0
        if baseparaconverter == 10 and numconvertido == 2:
            num = int(input('Digite o número: '))
            conversao = bin(num)

        elif baseparaconverter == 2 and numconvertido == 10:
            num = str(input('Digite o número (apenas uns e zeros): '))
            conversao = int(num, baseparaconverter)

        elif baseparaconverter == 10 and numconvertido == 8:
            num = int(input('Digite o número: '))
            conversao = oct(num)

        elif baseparaconverter == 8 and numconvertido == 10:
            num = str(input('Digite o número (apenas números de 0 a 7): '))
            conversao = int(num, baseparaconverter)

        elif baseparaconverter == 10 and numconvertido == 16:
            num = int(input('Digite o número: '))
            conversao = hex(num)

        elif baseparaconverter == 16 and numconvertido == 10:
            num = str(input('Digite o número (apenas números de 0 a 9 e letras de A até F): ')).upper()
            conversao = int(num, baseparaconverter)

        elif baseparaconverter == 2 and numconvertido == 8:
            num = str(input('Digite o número (apenas uns e zeros): '))
            conversao = oct(int(num, baseparaconverter))

        elif baseparaconverter == 8 and numconvertido == 2:
            num = str(input('Digite o número (apenas números de 0 a 7): '))
            conversao = bin(int(num, baseparaconverter))

        elif baseparaconverter == 8 and numconvertido == 16:
            num = str(input('Digite o número (apenas números de 0 a 7): '))
            conversao = hex(int(num, baseparaconverter))

        elif baseparaconverter == 16 and numconvertido == 8:
            num = str(input('Digite o número (apenas números de 0 a 9 e letras de A até F): ')).upper()
            conversao = oct(int(num, baseparaconverter))

        elif baseparaconverter == 16 and numconvertido == 2:
            num = str(input('Digite o número (apenas números de 0 a 9 e letras de A até F): ')).upper()
            conversao = bin(int(num, baseparaconverter))

        elif baseparaconverter == 2 and numconvertido == 16:
            num = str(input('Digite o número (apenas uns e zeros): '))
            conversao = hex(int(num, baseparaconverter))

        else:
            print('ERRO, Por favor, digite as bases numéricas corretamente')
            continue

        print('-=-=-=-=-')
        print('  ', conversao)
        print('-=-=-=-=-')

    return 'Fim do Programa'


print(conversor_numerico())

executar_novamente = input('Quer converter outro número? [S/N]: ').upper().strip()
while True:
    if 'S' in executar_novamente or 'SIM' in executar_novamente:
        print(conversor_numerico())
    elif 'N' in executar_novamente or 'NÃO' in executar_novamente or 'NAO' in executar_novamente:
        break
    else:
        executar_novamente = input('Não entendi. Por favor, digite S para sim ou N para não: ').upper().strip()

sleep(1.5)
