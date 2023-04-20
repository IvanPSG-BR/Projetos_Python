from time import sleep

print('=' * 36)
print('    CONVERSOR DE BASES NUMÉRICAS')
print('=' * 36)


def conversor_numerico():

    while True:
        sleep(2.0)
        print('''[ 1 ] Converter de decimal para binário
[ 2 ] Converter de binário para decimal
[ 3 ] Converter de decimal para octal
[ 4 ] Converter de octal para decimal
[ 5 ] Converter de decimal para hexadecimal
[ 6 ] Converter de hexadecimal para decimal
[ 7 ] Converter de binário para octal
[ 8 ] Converter de octal para binário
[ 9 ] Converter de octal para hexadecimal
[ 10 ] Converter de hexadecimal para octal
[ 11 ] Converter de hexadecimal para binário
[ 12 ] Converter de binário para hexadecimal
[ 0 ] Sair do programa''')
        sleep(2.0)

        opcao = int(input('Selecione uma opção: '))
        conversao = 0
        if opcao == 1:
            num = int(input('Digite um número: '))
            conversao = bin(num)

        elif opcao == 2:
            num = str(input('Número a ser convertido (apenas uns e zeros): '))
            conversao = int(num, 2)

        elif opcao == 3:
            num = int(input('Digite um número: '))
            conversao = oct(num)

        elif opcao == 4:
            num = str(input('Número a ser convertido (apenas números de 0 a 7): '))
            conversao = int(num, 8)

        elif opcao == 5:
            num = int(input('Digite um número: '))
            conversao = hex(num)

        elif opcao == 6:
            num = str(input('Número a ser convertido (apenas números de 0 a 9 e letras de A até F): ')).upper()
            conversao = int(num, 16)

        elif opcao == 7:
            num = str(input('Número a ser convertido (apenas uns e zeros): '))
            conversao = oct(int(num, 2))

        elif opcao == 8:
            num = str(input('Número a ser convertido (apenas números de 0 a 7): '))
            conversao = bin(int(num, 8))

        elif opcao == 9:
            num = str(input('Número a ser convertido (apenas números de 0 a 7): '))
            conversao = hex(int(num, 8))

        elif opcao == 10:
            num = str(input('Número a ser convertido (apenas números de 0 a 9 e letras de A até F): ')).upper()
            conversao = oct(int(num, 16))

        elif opcao == 11:
            num = str(input('Número a ser convertido (apenas números de 0 a 9 e letras de A até F): ')).upper()
            conversao = bin(int(num, 16))

        elif opcao == 12:
            num = str(input('Número a ser convertido (apenas números de 0 a 9 e letras de A até F): '))
            conversao = hex(int(num, 2))

        elif opcao == 0:
            break

        else:
            print('ERRO, Por favor, digite a opção corretamente')
            continue

        print('-=-=-=-=-')
        print('    ', conversao)
        print('-=-=-=-=-')

        return 'Fim do Programa'


print(conversor_numerico())

executar_novamente = input('Quer converter outro número? [S/N]: ').upper().strip()
while True:
    if 'S' in executar_novamente or 'SIM' in executar_novamente:
        print(conversor_numerico())
    elif 'N' in executar_novamente or 'NÃO' in executar_novamente:
        break
    else:
        executar_novamente = input('Não entendi. Por favor, digite S para sim ou N para não: ').upper().strip()

sleep(1.5)
