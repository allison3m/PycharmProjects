# PEDRA PAPEL TESOURA JOGO
from random import randint
from time import sleep
print('''ESCOLHA UMA OPÇÃO ENTRE:'
        [0] PEDRA '
        [1] PAPEL'
        [2]TESOURA''')
pc = randint(0 , 2)
item = ( 'Pedra' , 'Papel' , 'Tesoura')
jg = int((input('Qual a sua jogada:')))
print('JOOO')
sleep(1)
print('KEEENNNN')
sleep(2)
print('POOOOOO')
sleep(1)
print('-=' * 14)
sleep(1)
print('O computador escolheu {}'.format(item[pc]))
sleep(1)
print('E você escolheu {}'.format(item[jg]))
sleep(1)
print('-=' * 14)
if pc == 0 : # pc pedra
    if jg == 0 :
        print('\033[33mEMPATE\033[m!')
    elif jg == 1:
        print('\033[32mVOCÊ VENCEU!\033[m')
    elif jg == 2:
        print('\033[31mVOCÊ PERDEU\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 1 : # pc papel
    if jg == 0:
        print('\033[31mVOCÊ PERDEU\033[m!')
    elif jg == 1:
        print('\033[33mEMPATE\033[m!')
    elif jg == 2:
        print('\033[32mVOCÊ Vx  ENCEU!\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2: # pc tesoura
    if jg == 0:
        print('\033[32mVOCÊ VENCEU!\033[m')
    elif jg == 1:
        print('\033[31mVOCÊ PERDEU\033[m')
    elif jg == 2:
        print('\033[33mEMPATE\033[m!')
    else:
        print('JOGADA INVÁLIDA')
    sleep(20)









