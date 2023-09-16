from time import sleep

cor8 = {'azul':'\033[0:34m',
        'amarelo':'\033[1:33m',
        'roxo':'\033[1:35m',
        'ciano':'\033[1:36m',
        'vermelho':'\033[1:31:40m',
        'azul2':'\033[1:34m'}

sleep(2)
print('{}Sinto muito Sr(a)!{}'.format(cor8['azul2'], '\033[m'))
while True:
    print('{}[1] - SEM PROBLEMAS!'.format(cor8['roxo'], '\033[m'))
    op = int(input('{}OPÇÃO:{} '.format(cor8['amarelo'], '\033[m')))
    if op == 1:
        break
        sleep(2)
    else:
        print('{}Opção invalida. Tente novamente{}'.format(cor8['azul2'], '\033[m'))

sleep(2)
print('{}O pedido não foi aprovado pelo fato das parcelas comprometerem 30% do salario do Sr(a).{}'.format(cor8['azul2'], '\033[m'))
while True:
    print('{}[1] - EU JA IMAGINAVA ISSO.'.format(cor8['roxo'], '\033[m'))
    op = int(input('{}OPÇÃO:{} '.format(cor8['amarelo'], '\033[m')))
    if op == 1:
        print('{}Mais tem outra possibilidae..{}'.format(cor8['azul2'], '\033[m'))
        break
        sleep(2)
    else:
        print('{}Opção invalida. Tente novamente{}'.format(cor8['azul2'], '\033[m'))
        sleep(2)

sleep(2)
print('{}Podemos agendar uma visita para tentarmos novamente?{}'.format(cor8['azul2'], '\033[m'))
sleep(2)
op = 0
while True:
    print('{}[1] - CLARO! VAMOS SIM?'.format(cor8['roxo'], '\033[m'))
    print('[2] - VOU PENSAR NO ASSUNTO E DEPOIS RESPONDO.{}'.format(cor8['roxo'], '\033[m'))
    op = int(input('{}OPÇÃO:{} '.format(cor8['amarelo'], '\033[m')))
    if op == 1:
        print('{}Perfeito! Estarie entrando em contato para agendarmos um visita..{}'.format(cor8['azul2'], '\033[m'))
        break
        sleep(2)
    elif op == 2:
        print('{}Esta ok entao. Fico no aguardo.{}'.format(cor8['azul2'], '\033[m'))
        sleep(2)
        break
    else:
        print('{}Opção invalida. Tente novamente{}'.format(cor8['azul2'], '\033[m'))
        sleep(2)

sleep(2)
print('{}Estarei encerrando o atendimento.{}'.format(cor8['azul2'], '\033[m'))
print('{}Que o sr(a) tenha um dia abençoado.{}'.format(cor8['azul2'], '\033[m'))
sleep(2)
op = 0
while True:
    print('{}[1] - AMEM! IGUALMENTE'.format(cor8['roxo'], '\033[m'))
    op = int(input('{}OPÇÃO:{} '.format(cor8['amarelo'], '\033[m')))
    if op == 1:
        print('{}Obrigada, AMÉM{}'.format(cor8['azul2'], '\033[m'))
        break
        sleep(2)
    else:
        print('{}Opção invalida. Tente novamente{}'.format(cor8['azul2'], '\033[m'))
        sleep(2)

Perguntas4 = {
    '{}SUA OPNIÃO É MUITO IMPORTANTE{}'.format(cor8['ciano'], '\033[m'):{
        'Maria': '{}Qual nota o Sr(a) da para o nosso atendimento?:{}'.format(cor8['amarelo'], '\033[m'),
        'respostas':{'1': '{}RUIM{}'.format(cor8['roxo'], '\033[m'), '2': '{}MEDIA{}'.format(cor8['roxo'], '\033[m'), '3': '{}BOA{}'.format(cor8['roxo'], '\033[m'),
                     '4': '{}ÓTIMA{}'.format(cor8['roxo'], '\033[m'), '5': '{}EXCELENTE{}'.format(cor8['roxo'], '\033[m')},
        'Digite a opção desejada': ' ',
    },

}
print()

respostas_certas = 0
for cp,  cr in Perguntas4.items():
    print(f'{cp}: {cr["Maria"]}')
    sleep(1)

    print('{}Escolha uma das opções:{} '.format(cor8['azul2'], '\033[m'))
    for rp, rr in cr['respostas'].items():
        sleep(1)
        print(f'[{rp}]: {rr}')

    resposta_correta = input('{}OPÇÃO:{} '.format(cor8['amarelo'], '\033[m'))

    if resposta_correta == cr:
        print('{}A AUTORAIO AGRADEÇE, TENHA UM OTIMO DIA.{}'.format(cor8['vermelho'], '\033[m'))
        sleep(1)
        respostas_certas += 1
    else:
        print('{}A AUTORAIO AGRADEÇE, TENHA UM OTIMO DIA.{}'.format(cor8['vermelho'], '\033[m'))
        sleep(1)

    print()

print('-=' * 20)
#print(emoji.emojize('SEJA BEM VINDO A AUTORAIO :car:', language='alias'))
print('     {} ATENCIOSAMENTE AUTORAIO {}'.format(cor8['vermelho'], '\033[m'))
print('-=' * 20)