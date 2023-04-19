from setuptools import setup, find_packages

setup(
    name='Projetos Python',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dificuldade_jogodaadivinhacao = Jogo_da_Advinhação:dificuldade_do_jogo'
            'jogar_jogodaadivinhacao = Jogo_da_Advinhação:jogo_da_adivinhacao'
            'jogo_rodando = Jogo_da_Advinhação:execucao_do_jogo'
        ]
    },
    install_requires=[
        'time',
        'random'
    ]
)