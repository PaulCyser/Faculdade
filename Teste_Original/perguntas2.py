from time import sleep

cor5 = {'azul':'\033[0:34m',
        'amarelo':'\033[1:33m',
        'roxo':'\033[1:35m',
        'azul2':'\033[1:34m'}

Perguntas2 = {
    '{}DE ACORDO COM OS VEICULOS DISPONIVEIS ACIMA{}'.format(cor5['amarelo'], '\033[m'):{
        'Maria': '{}Podemos dar inicio ao simulado?{}'.format(cor5['azul2'], '\033[m'),
        'respostas':{'1': '{}VAMOS SIM, CLARO!{}'.format(cor5['roxo'], '\033[m'), '2': '{}ACHO MELHOR NÃO{}'.format(cor5['roxo'], '\033[m')},
        'Digite a opção desejada': ' '},
    '{}IMPORTANTE{}'.format(cor5['amarelo'], '\033[m'):{
        'Maria': '{}Não é necessario ponto ou virgula no preenchimento{}'.format(cor5['azul2'], '\033[m'),
        'respostas':{'1': '{}OK{}'.format(cor5['roxo'], '\033[m')},
        'Digite a opção desejada': ' '},
    '{}OUTRO PONTO IMPORTANTE{}'.format(cor5['amarelo'], '\033[m'):{
        'Maria': '{}É que o juros inicial é de acordo com a quantidade de parcelas,'
                 'O Sr(a) está de acordo com isso?{}'.format(cor5['azul2'], '\033[m'),
        'respostas':{'1': '{}ESTOU SIM{}'.format(cor5['roxo'], '\033[m'), '2': '{}MELHOR NÃO{}'.format(cor5['roxo'], '\033[m')},
        'Digite a opção desejada': ' '},

}
print()

respostas_certas = 0
for cp,  cr in Perguntas2.items():
    print(f'{cp}: {cr["Maria"]}')
    sleep(1)

    print('{}Escolha uma das opções:{} '.format(cor5['azul2'], '\033[m'))
    sleep(1)
    for rp, rr in cr['respostas'].items():
        print(f'[{rp}]: {rr}')
        sleep(1)

    resposta_correta = input('{}OPÇÃO:{} '.format(cor5['amarelo'], '\033[m'))

    if resposta_correta == cr['Digite a opção desejada']:
        sleep(1)
        print('{}Maravilha, vamos continuar.{}'.format(cor5['azul2'], '\033[m'))
        respostas_certas += 1
    else:
        print('{}Maravilha, vamos continuar.{}'.format(cor5['azul2'], '\033[m'))
        sleep(1)

    print()