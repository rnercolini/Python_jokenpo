# Game Jokenpô.
from random import randint
from time import sleep
import emoji
print('''Escolha uma opção para jogar com o computador:
      \033[34m[ 0 ] Pedra
      [ 1 ] Papel
      [ 2 ] Tesoura\033[m''')
usuario = int(input('Digite a opção: '))

if usuario >= 0 and usuario <= 2 and usuario != '':
    pc = randint(0, 2)
    lista = ('Pedra', 'Papel', 'Tesoura')
    sleep(0.5)
    print('\033[32mJo...{:2}'.format(emoji.emojize(':punch:', language='alias')))
    sleep(1)
    print('Ken...{:2}'.format(emoji.emojize(':hand:', language='alias')))
    sleep(1)
    print('Pô!\033[m{:2}'.format(emoji.emojize(':v:', language='alias')))
    sleep(0.5)
    print('\033[34m*\033[m' * 30)
    print('Você escolheu \033[31m{}\033[m.'.format(lista[usuario]))
    sleep(0.5)
    print('O computador escolheu \033[31m{}\033[m.'.format(lista[pc]))
    sleep(0.5)
    print('\033[34m*\033[m' * 30)
    if usuario == 0 and pc == 0:
        print('\033[31mDeu empate!\033[m {}'.format(emoji.emojize(':handshake:', language='alias')))
    elif usuario == 0 and pc == 1:
        print('\033[31mO computador ganhou!\033[m {}'.format(emoji.emojize(':robot:', language='alias')))
    elif usuario == 0 and pc == 2:
        print('\033[31mVocê ganhou!\033[m {}'.format(emoji.emojize(':1st_place_medal:', language='alias')))
    elif usuario == 1 and pc == 0:
        print('\033[31mVoce ganhou!\033[m {}'.format(emoji.emojize(':1st_place_medal:', language='alias')))
    elif usuario == 1 and pc == 1:
        print('\033[31mDeu empate!\033[m {}'.format(emoji.emojize(':handshake:', language='alias')))
    elif usuario == 1 and pc == 2:
        print('\033[31mO computador ganhou!\033[m {}'.format(emoji.emojize(':robot:', language='alias')))
    elif usuario == 2 and pc == 0:
        print('\033[31mO computador ganhou!\033[m {}'.format(emoji.emojize(':robot:', language='alias')))
    elif usuario == 2 and pc == 1:
        print('\033[31mVocê ganhou!\033[m {}'.format(emoji.emojize(':1st_place_medal:', language='alias')))
    elif usuario == 2 and pc == 2:
        print('\033[31mDeu empate!\033[m {}'.format(emoji.emojize(':handshake:', language='alias')))
else:
    print('\033[31mEscolha uma opção de 0 a 2 e tente novamente!\033[m')
