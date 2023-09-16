from time import sleep

cor2 = {'azul':'\033[0:34m',
        'amarelo':'\033[1:33m',
        'roxo':'\033[1:35m',
        'azul2':'\033[1:34m'}

Perguntas = {
    '{}SOBRE SEUS BENS{}'.format(cor2['amarelo'], '\033[m'):{
        'Maria': '{}O Sr(a) possui carro ou moto em seu nome?{}'.format(cor2['azul2'], '\033[m'),
        'respostas':{'1': '{}SIM, carro e moto{}'.format(cor2['roxo'], '\033[m'), '2': '{}SIM, apenas carro{}'.format(cor2['roxo'], '\033[m'),
                     '3': '{}SIM, apenas moto{}'.format(cor2['roxo'], '\033[m').format(cor2['roxo'], '\033[m'), '4': '{}NÃO{}'.format(cor2['roxo'], '\033[m')},
        '{}Digite a opção desejada:{}': ' ',
    },
    '{}SOBRE CASA{}'.format(cor2['amarelo'], '\033[m'):{
        'Maria': '{}O Sr(a) possui casa em seu nome?{}'.format(cor2['azul2'], '\033[m'),
        'respostas':{'1': '{}SIM{}'.format(cor2['roxo'], '\033[m'), '2': '{}NÃO{}'.format(cor2['roxo'], '\033[m')},
        'Digite a opção desejada': ' ',
    },
    '{}SOBRE O BANCO{}'.format(cor2['amarelo'], '\033[m'):{
        'Maria': '{}O Sr(a) tem conta em qual banco?{}'.format(cor2['azul2'], '\033[m'),
        'respostas':{'1': '{}BRADESCO{}'.format(cor2['roxo'], '\033[m'), '2': '{}CAIXA{}'.format(cor2['roxo'], '\033[m'), '3': '{}ITAU{}'.format(cor2['roxo'], '\033[m'),
                     '4': '{}SANTANDER{}'.format(cor2['roxo'], '\033[m'), '5': '{}SAFRA{}'.format(cor2['roxo'], '\033[m'),
                     '6': '{}BANCO DO BRASIL{}'.format(cor2['roxo'], '\033[m'), '7': '{}OUTRO{}'.format(cor2['roxo'], '\033[m')},
        'Digite a opção desejada': ' ',
    },
    '{}SOBRE A TABELA DE PREÇOS{}'.format(cor2['amarelo'], '\033[m'):{
        'Maria': '{}Enviarei a tabela com os carros que temos disponiveis, com o ano e o preço de cada um deles.{}'.format(cor2['azul2'], '\033[m'),
        'respostas':{'1': '{}MARAVILHA{}'.format(cor2['roxo'], '\033[m')},
        'Digite a opção desejada': ' ',
    },

}
print()

respostas_certas = 0
for cp,  cr in Perguntas.items():
    print(f'{cp}: {cr["Maria"]}')
    sleep(1)

    print('{}Escolha uma das opções:{} '.format(cor2['amarelo'], '\033[m'))
    for rp, rr in cr['respostas'].items():
        sleep(1)
        print(f'[{rp}]: {rr}')

    resposta_correta = input('{}OPÇÃO:{} '.format(cor2['amarelo'], '\033[m'))
    sleep(1)

    if resposta_correta == cr:
        print('{}Maravilha, vamos continuar.{}'.format(cor2['azul2'], '\033[m'))
        respostas_certas += 1
        sleep(1)
    else:
        print('{}Maravilha, vamos continuar.{}'.format(cor2['azul2'], '\033[m'))
        sleep(1)