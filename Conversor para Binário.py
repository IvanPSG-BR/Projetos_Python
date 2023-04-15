from time import sleep

print('=' * 29)
print('    CONVERSOR EM BINÁRIO')
print('=' * 29)

while True:
    sleep(2.0)
    print('''[ 1 ] Converter de decimal para binário
[ 2 ] Converter de binário para decimal
[ 3 ] Converter de decimal para hexadecimal
[ 4 ] Converter de hexadecimal para decimal
[ 0 ] Sair do programa''')
    sleep(2.0)
    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        num = int(input('Digite um número: '))
        decparabin = bin(num)
        print('-=-=-=-=-')
        print(decparabin)
        print('-=-=-=-=-')

    elif opcao == 2:
        num = str(input('Número a ser convertido (apenas uns e zeros): '))
        binparadec = int(num, 2)
        print('-=-=-=-=-')
        print(binparadec)
        print('-=-=-=-=-')

    elif opcao == 3:
        num = int(input('Digite um número: '))
        decparahexa = hex(num)
        print('-=-=-=-=-')
        print(decparahexa)
        print('-=-=-=-=-')

    elif opcao == 4:
        num = str(input('Número a ser convertido (apenas números de 1 a 10 e letras de A até F): ')).upper()
        hexaparadec = int(num, 16) + 1
        print('-=-=-=-=-')
        print(hexaparadec)
        print('-=-=-=-=-')

    elif opcao == 0:
        break

    else:
        print('ERRO, Por favor, digite a opção corretamente')

print('Fim do Programa')
sleep(5.0)
