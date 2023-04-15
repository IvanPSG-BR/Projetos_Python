from time import sleep
from random import choice
from re import sub

"""Importa o comando sleep para fazer o programa demorar um pouco de executar o código com pausas;
O comando choice pra escolher um item aleatório da lista; 
E o comando sub substitui caracteres de uma variável por outro"""

frutas = ['Abacate', 'Abacaxi', 'Acerola', 'Ameixa', 'Banana', 'Cacau', 'Caju', 'Cereja', 'Cupuaçu', 'Caqui',
          'Damasco', 'Framboesa', 'Figo', 'Goiaba', 'Groselha', 'Jabuticaba', 'Jenipapo', 'Kiwi', 'Laranja',
          'Limão', 'Manga', 'Melancia', 'Morango', 'Pera', 'Pitaia', 'Tangerina', 'Tamarindo', 'Uva', 'Umbu']

paises = ['Alemanha', 'Angola', 'Argentina', 'Brasil', 'Chile', 'China', 'Coreia Do Sul', 'Cuba', 'Dinamarca', 'Egito',
          'Equador', 'Inglaterra', 'Iraque', 'Irlanda', 'Israel', 'Luxemburgo', 'Madagascar', 'Noruega', 'Paraguai',
          'Peru', 'Portugal', 'Qatar', 'Uruguai', 'Venezuela']

cores = ['Amarelo', 'Azul', 'Bege', 'Branco', 'Carmim', 'Ciano', 'Cinza', 'Dourado', 'Escarlate', 'Laranja', 'Magenta',
         'Marrom', 'Prateado', 'Preto', 'Rosa', 'Roxo', 'Turquesa', 'Verde', 'Vermelho', 'Vinho', 'Violeta']

roupas = ['Bermuda', 'Blusa', 'Boina', 'Bota', 'Calcinha', 'Calça', 'Camisa', 'Capuz', 'Casaco', 'Chinelo', 'Cinto',
          'Gorro', 'Jaleco', 'Jaqueta', 'Luva', 'Manto', 'Meia', 'Pijama', 'Regata', 'Saia', 'Sapato', 'Vestido']

partescorpo = ['Axilas', 'Barriga', 'Boca', 'Bochechas', 'Braços', 'Bunda', 'Cabelo', 'Cabeça', 'Calcanhar',
               'Cílios', 'Cintura', 'Costas', 'Cotovelo', 'Coxa', 'Dedos', 'Nariz', 'Olhos', 'Ombros',
               'Orelhas', 'Peito', 'Pernas', 'Pescoço', 'Queixo', 'Testa', 'Tornozelo',
               'Umbigo', 'Vagina']

profissoes = ['Advogado', 'Arquiteto', 'Assistente social', 'Atendente', 'Auditor', 'Barbeiro', 'Bombeiro',
              'Cabeleireiro', 'Camareiro', 'Carpinteiro', 'Chef De Cozinha',
              'Comerciante', 'Contador', 'Corretor', 'Cozinheiro', 'Dentista', 'Designer',
              'Desenvolvedor', 'Diretor', 'Economista', 'Eletricista', 'Enfermeiro', 'Engenheiro', 'Fisioterapeuta',
              'Garçom', 'Jardineiro', 'Jornalista', 'Juiz', 'Nutricionista', 'Professor', 'Recepcionista']
temas = [frutas, paises, cores, roupas, partescorpo, profissoes]
# Listas com as palavras e lista com todas as listas

palavra = palavraoculta = chute = tentarpalavra = adivinhar_imediatamente = jogardenovo = ''
# Define todas essas variáveis como strings vazias para serem modificadas mais pra frente

while True:
    tentativaletra = ''
    erros = 6
    # Quantidade de vezes que o usuário pode errar a letra

    # Enquanto o loop não for quebrado (interrompido)
    print("""Bem vindo ao jogo da forca. Selecione o tema desejado:
[ 1 ] Frutas
[ 2 ] Países
[ 3 ] Cores
[ 4 ] Roupas
[ 5 ] Partes do Corpo
[ 6 ] Profissões
[ 7 ] Tema Aleatório
[ 0 ] Sair do Programa""")
    opcao = int(input('Sua Escolha: '))
    # Mostra as opções de temas para escolher a palavra da lista escolhida pelo usuário na variável "opcao"

    while opcao > 7 or opcao < 0:
        opcao = int(input('Digite uma opcao valida: '))
        # Enquanto o número digitado na variável não estiver dentre os apresentados, não será um número válido
    if opcao == 0:
        break
        # Interrompe o loop e finaliza o programa se a opção escolhida for 0 (Sair do Programa)
    elif opcao == 7:
        palavra = choice(choice(temas))
        # Escolhe uma palavra aleatória de uma lista também aleatória se a opção escolhida for 7 (Tema Aleatório)
    else:
        palavra = choice(temas[opcao - 1])
        # Escolhe uma palavra aleatória do tema escolhido

    palavraoculta = sub('[a-zA-Z]', '_', palavra)
    # Esconde o conteúdo da palavra, substituindo todas as letras (apenas letras) pelo caractere '_'

    print('Já escolhi a palavra. Você pode errar a letra até 6 vezes. Boa sorte!')
    print(f'Palavra secreta: {palavraoculta}')

    while palavraoculta != palavra or erros == 0:
        chute = input(f'Você ainda tem {erros} chances. Qual letra você chuta? ')
        """Enquanto a palavra que está oculta for diferente da palavra normal, e o número de erros for menor que 7,
        O código principal do jogo é executado, começando pela pergunta ao usuário de qual letra ele chuta"""

        if chute.isalpha() is True and len(chute) == 1:
            # Apenas executa o código se o caractere digitado fizer parte do alfabeto e se for só 1 caractere
            if chute in tentativaletra:
                print('Você já tentou essa letra, tente outra.')
                print(palavraoculta)
                continue
            else:
                tentativaletra += chute
            """Se a pessoa chutar uma letra que já foi chutada antes o programa avisa 
            Senão, a letra é adicionada a variável "tentativaletra" """

            if chute.lower().strip() in palavra.lower().strip():
                indiceletra = [i for i, letra in enumerate(palavra) if letra.lower() == chute.lower()]
                for indice in indiceletra:
                    palavraoculta = palavraoculta[:indice] + palavra[indice] + palavraoculta[indice + 1:]
            else:
                erros -= 1
                print(f'Você errou. Tente novamente...')
            """Por ser complexo irei falar apenas o que basicamente faz, 
            Que é verificar cada letra da palavra pra saber se é igual ao chute, 
            E se caso for, o programa revela a letra chutada em todas as posições que ela se encontra na palavra
            Caso não for, o usuário perde uma tentativa de chutar a letra e é avisado que ele errou a letra"""

        else:
            print('Isso não é uma letra. Tente novamente')
            """Se o chute for mais de um caractere e não fizer parte do alfabeto, 
            O programa diz que não é uma letra e o loop é repetido"""

        print(palavraoculta)
        # Mostra o estado atual da palavra misteriosa

        tentarpalavra = input('Quer tentar advinhar a palavra? Se acertar, ganhará o jogo imediatamente, porém se errar'
                              ' você perde. [S/N]: ').upper().strip()
        # Pergunta se o usuário quer tentar adivinhar a palavra com o que já sabe.

        while True:
            if 'S' in tentarpalavra or 'SIM' in tentarpalavra:
                adivinhar_imediatamente = input('Sua tentativa: ').title().strip()
                break
            elif 'N' in tentarpalavra or 'NÃO' in tentarpalavra:
                print(f'Ok, então continue o jogo\n{palavraoculta}')
                break
            else:
                tentarpalavra = input('Não entendi. Por favor, digite S para sim ou N para não: ').upper().strip()
            """Enquanto o loop não for quebrado, 
            Se a resposta for sim, o usuário digita a palavra desejada e o loop termina
            Se a resposta for não, o jogo continua e o loop termina
            Se a resposta for diferente de sim ou não, o programa pede para digitar uma entrada válida"""

        if 'S' in tentarpalavra or 'SIM' in tentarpalavra:
            if adivinhar_imediatamente == palavra or palavraoculta == palavra and erros < 7:
                print(f'Parabéns, você acertou com {6 - erros} erros! A palavra é {palavra}')
                break
            elif adivinhar_imediatamente != palavra:
                print(f'Que pena, não foi dessa vez. A palavra era {palavra}')
                break
            elif erros == 0:
                print(f'Bem, acabaram suas tentativas, a palavra era {palavra}.')
                break
        """Aqui diz se o usuário acertou a palavra (revelando a palavra e informando a quantidade de erros), 
        Se errou a palavra ou se esgotou suas tentativas, também revelando a palavra.
        Nas três possibilidades o loop é interrompido"""

    jogardenovo = input('Quer Jogar novamente? [S/N]: ').upper().strip()
    # Pergunta se o usuário quer jogar novamente,

    if 'S' in jogardenovo or 'SIM' in jogardenovo:
        sleep(2.0)
        continue
    elif 'N' in jogardenovo or 'NÃO' in jogardenovo:
        break
    else:
        jogardenovo = input('Não entendi. Por favor, digite S para sim ou N para não: ').upper().strip()
    # Se sim, o jogo reinicia, se não ele é finalizado; e se não for nenhuma das opções o programa pede para repetir

print('Até mais!')
sleep(5.0)
# Fim do programa!
