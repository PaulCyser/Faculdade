from tkinter import *
from time import sleep

#import emoji
cor = {'vermelho':'\033[1:31:40m'}

print('-=' * 20)
#print(emoji.emojize('SEJA BEM VINDO A AUTORAIO :car:', language='alias'))
print('     {} SEJA BEM VINDO A AUTORAIO {}'.format(cor['vermelho'], '\033[m'))
print('-=' * 20)

sleep(2)

cor1 = {'azul':'\033[0:34m',
        'amarelo':'\033[1:33m',
        'roxo':'\033[1:35m',
        'azul2':'\033[1:34m'}

print('{}OLÁ, ME CHAMO MARIA, COM QUEM EU  FALO?{}'.format(cor1['azul2'], '\033[m'))
sleep(2)

nm = str(input())
sleep(2)

print('{}MUITO PRAZER EM TE CONHECER, {}{}.'.format(cor1['azul2'], nm, '\033[m'))
sleep(2)

print('{}TUDO BEM COM O SR(a)?{}'.format(cor1['azul2'], '\033[m'))
sleep(2)

op = 0
while True:
    print('{}[1] - ESTOU BEM SIM, E VOCÊ?'.format(cor1['roxo'], '\033[m'))
    sleep(2)
    print('[2] - NÃO ESTOU MUITO BEM.{}'.format(cor1['roxo'], '\033[m'))
    sleep(2)

    op = int(input('{}OPÇÃO:{} '.format(cor1['amarelo'], '\033[m')))
    if op == 1:
        print('{}QUE BOM, EU ESTOU BEM TAMBEM..{}'.format(cor1['azul2'], '\033[m'))
        sleep(2)
        break
    elif op == 2:
        print('{}QUE PENA, MAIS LOGO LOGO TUDO MELHORA.{}'.format(cor1['azul2'], '\033[m'))
        sleep(2)
        break
    else:
        print('{}OPÇÃO INVALIDA. TENTE NOVAMENTE.{}'.format(cor1['azul2'], '\033[m'))
        sleep(3)
        from saudação import op
        sleep(2)

print('{}EM QUE POSSO AJUDAR?{}'.format(cor1['azul2'], '\033[m'))
sleep(2)

opcao = 0
while True:
    print('{}[1] - SIMULADO'.format(cor1['roxo'], '\033[m'))
    sleep(2)
    opcao = int(input('{}OPÇÃO:{} '.format(cor1['amarelo'], '\033[m')))
    if opcao == 1:
        print('{}PERFEITO, VAMOS CONTINUAR.{}'.format(cor1['azul2'], '\033[m'))
        break
    else:
        print('{}OPÇÃO INVALIDA. TENTE NOVAMENTE.{}'.format(cor1['azul2'], '\033[m'))
    sleep(2)

sleep(2)

print('{}VOU PRECISAR DE ALGUNS DADOS OK?{}'.format(cor1['azul2'], '\033[m'))
print('{}1 - PERFEITO.{}'.format(cor1['roxo'], '\033[m'))
sim_nao = int(input('{}OPÇÃO:{} '.format(cor1['amarelo'], '\033[m')))
if sim_nao == 1:
    print('{}ENTÃO VAMOS COMECAR!{}'.format(cor1['azul2'], '\033[m'))
    print('{}CARREGANDO..............{}'.format(cor1['roxo'], '\033[m'))
    sleep(4)