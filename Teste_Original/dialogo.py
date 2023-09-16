from time import sleep

cor7 = {'azul':'\033[0:34m',
        'amarelo':'\033[1:33m',
        'roxo':'\033[1:35m',
        'ciano':'\033[1:36m',
        'vermelho':'\033[1:31:40m',
        'azul2':'\033[1:34m'}

print('{}É uma sensação maravilhosa não é Sr(a)?{}'.format(cor7['azul2'], '\033[m'))
op = 0
while True:
    print('{}[1] - Muito maravilhosa mesmo, voces sao demais.'.format(cor7['roxo'], '\033[m'))
    op = int(input('{}OPÇÃO:{} '.format(cor7['amarelo'], '\033[m')))
    if op == 1:
        print('{}Eu imagino como seja a sensação.{}'.format(cor7['azul2'], '\033[m'))
        break
        sleep(2)
    else:
        print('{}Opção invalida. Tente novamente{}'.format(cor7['azul2'], '\033[m'))


sleep(2)
print('{}Gostaria de está parabenizando o sr(a) pela compra.{}'.format(cor7['azul2'], '\033[m'))
sleep(2)
op = 0
while True:
    print('{}[1] - Muito Obrigado, voces sao demais.'.format(cor7['roxo'], '\033[m'))
    op = int(input('{}OPÇÃO:{} '.format(cor7['amarelo'], '\033[m')))
    if op == 1:
        print('{}Obrigado o Sr(a) pela preferencia.{}'.format(cor7['azul2'], '\033[m'))
        break
    else:
        print('{}Opção invalida. Tente novamente{}'.format(cor7['azul2'], '\033[m'))

sleep(2)
print('{}Estarei entrando em contato atraves de ligação ou whatsapp para agendarmos sua visita.{}'.format(cor7['azul2'], '\033[m'))
op = 0
while True:
    print('{}[1] - Perfeito! Ficarei no aguardo.'.format(cor7['roxo'], '\033[m'))
    op = int(input('{}OPÇÃO:{} '.format(cor7['amarelo'], '\033[m')))
    if op == 1:
        print('{}Para acertarmos tudo e o sr(a) retirar o seu veiculo..{}'.format(cor7['azul2'], '\033[m'))
        break
    else:
        print('{}Opção invalida. Tente novamente{}'.format(cor7['azul2'], '\033[m'))

sleep(2)
print('{}Que o sr(a) tenha um dia abençoado.{}'.format(cor7['azul2'], '\033[m'))
sleep(2)
op = 0
while True:
    print('{}[1] - AMEM! IGUALMENTE'.format(cor7['roxo'], '\033[m'))
    op = int(input('{}OPÇÃO:{} '.format(cor7['amarelo'], '\033[m')))
    if op == 1:
        print('{}Obrigada, AMÉM{}'.format(cor7['azul2'], '\033[m'))
        break
        sleep(2)
    else:
        print('{}Opção invalida. Tente novamente{}'.format(cor7['azul2'], '\033[m'))
        sleep(2)

sleep(2)

Perguntas4 = {
    '{}SUA OPNIÃO É MUITO IMPORTANTE{}'.format(cor7['ciano'], '\033[m'):{
        'Maria': '{}Qual nota o Sr(a) da para o nosso atendimento?:{}'.format(cor7['amarelo'], '\033[m'),
        'respostas':{'1': '{}RUIM{}'.format(cor7['roxo'], '\033[m'), '2': '{}MEDIA{}'.format(cor7['roxo'], '\033[m'), '3': '{}BOA{}'.format(cor7['roxo'], '\033[m'),
                     '4': '{}ÓTIMA{}'.format(cor7['roxo'], '\033[m'), '5': '{}EXCELENTE{}'.format(cor7['roxo'], '\033[m')},
        'Digite a opção desejada': ' ',
    },

}
print()

respostas_certas = 0
for cp,  cr in Perguntas4.items():
    print(f'{cp}: {cr["Maria"]}')
    sleep(1)

    print('{}Escolha uma das opções:{} '.format(cor7['azul2'], '\033[m'))
    for rp, rr in cr['respostas'].items():
        sleep(1)
        print(f'[{rp}]: {rr}')

    resposta_correta = input('{}OPÇÃO:{} '.format(cor7['amarelo'], '\033[m'))

    if resposta_correta == cr:
        print('{}A AUTORAIO AGRADEÇE, TENHA UM OTIMO DIA.{}'.format(cor7['vermelho'], '\033[m'))
        sleep(1)
        respostas_certas += 1
    else:
        print('{}A AUTORAIO AGRADEÇE, TENHA UM OTIMO DIA.{}'.format(cor7['vermelho'], '\033[m'))
        sleep(1)

    print()

print('-=' * 20)
#print(emoji.emojize('SEJA BEM VINDO A AUTORAIO :car:', language='alias'))
print('     {} ATENCIOSAMENTE AUTORAIO {}'.format(cor7['vermelho'], '\033[m'))
print('-=' * 20)

