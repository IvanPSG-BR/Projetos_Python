from time import sleep

print('=' * 29)
print('    CONVERSOR EM BINÁRIO')
print('=' * 29)
num = int(input('Digite um número: '))

while True:
    sleep(2.0)
    print('''[ 1 ] Converter de decimal para binário
[ 2 ] Converter de binário para decimal (Digitar o número novamente)
[ 3 ] Novo número
[ 4 ] Sair do programa''')
    sleep(2.0)
    opcao = int(input('Selecione uma opção: '))
    decparabin = bin(num)
    if opcao == 1:
        print('-=-=-=-=-')
        print(decparabin)
        print('-=-=-=-=-')

    elif opcao == 2:
        num = str(input('Número a ser convertido (apenas uns e zeros): '))
        binparadec = int(num, 2)
        print(binparadec)

    elif opcao == 3:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-')
        num = int(input('Insira um novo número: '))
        print('-=-=-=-=-=-=-=-=-=-=-=-=-')

    elif opcao == 4:
        break

    else:
        print('ERRO, Por favor, digite a opção corretamente')

print('Fim do Programa')
