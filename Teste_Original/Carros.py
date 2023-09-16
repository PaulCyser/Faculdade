from time import sleep

cores = {'azul':'\033[0:34m',
        'amarelo':'\033[1:33m',
        'roxo':'\033[1:35m',
        'azul2':'\033[1:34m'}

print('{}Qual a marca de carro que o sr(a) deseja compra?{}'.format(cores['azul2'], '\033[m'))
sleep(1)
print('{}1 - AUDI{}'.format(cores['roxo'], '\033[m'))
sleep(1)
print('{}2 - CHEVROLET{}'.format(cores['roxo'], '\033[m'))
sleep(1)
print('{}3 - CITROËN{}'.format(cores['roxo'], '\033[m'))
sleep(1)
print('{}4 - FIAT{}'.format(cores['roxo'], '\033[m'))
sleep(1)
print('{}5 - FORD{}'.format(cores['roxo'], '\033[m'))
sleep(1)
print('{}6 - HONDA{}'.format(cores['roxo'], '\033[m'))
sleep(1)
print('{}7 - HYUNDAI{}'.format(cores['roxo'], '\033[m'))
sleep(1)
print('{}8 - PEUGEOT{}'.format(cores['roxo'], '\033[m'))
sleep(1)
print('{}9 - RENAULT{}'.format(cores['roxo'], '\033[m'))
sleep(1)
print('{}10- TOYOTA{}'.format(cores['roxo'], '\033[m'))
sleep(1)
print('{}11 - VOLKSWAGEM{}'.format(cores['roxo'], '\033[m'))

carro = int(input('{}Digite a opção desejada:{} '.format(cores['amarelo'], '\033[m')))

if carro == 1:
    print('{}CARREGANDO OS CARROS DISPONIVEIS ......{}'.format(cores['amarelo'], '\033[m'))
    sleep(2)
    print('{}ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:{}'.format(cores['azul2'], '\033[m'))
    print('''{}
[1] - 'Carro: Audi A3, Preço: R$ 124.900,00, Ano: 2018'
[2] - 'Carro: Audi A4, Preço: R$ 172.990,00, Ano: 2017{}'''.format(cores['roxo'], '\033[m'))
    sleep(3)

elif carro == 2:
    print('{}CARREGANDO OS CARROS DISPONIVEIS ......{}'.format(cores['amarelo'], '\033[m'))
    sleep(3)
    print('{}ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:{}'.format(cores['azul2'], '\033[m'))
    print('''{}
[1] - Carro: Celta, Preço: R$ 16202, Ano: 2012
[2] - Carro: Corsa, Preço: R$ 20.500,00, 'Ano': 2012
[3]  - Carro: Corsa Classic, Preço: R$ 30.500,00, 'Ano': 2012
[4] - Carro: Cruze, Preço: R$ 89.900,00, Ano: 2017 
[5] - Carro: Joy, Preço: R$ 50.090,00, 'Ano': 2019
[6] - Carro: Onix, Preço: R$ 67.900,00, 'Ano': 2018{}'''.format(cores['roxo'], '\033[m'))
elif carro == 3:
    print('{}CARREGANDO OS CARROS DISPONIVEIS ......{}'.format(cores['amarelo'], '\033[m'))
    sleep(3)
    print('{}ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:{}'.format(cores['azul2'], '\033[m'))
    print('''{}
[1] - Carro: C3, Preço: R$ 44.000,00, Ano: 2019
[2] - Carro: C3 Picasso, Preço: R$ 48.000,00, Ano: 2017
[3] - Carro: C4 Cactus, Preço: R$ 69.000,00, Ano: 2018,
[4] - Carro: C4 Picasso, Preço: R$ 125.000,00, Ano: 2019
[5] - Carro: C4, Preço: R$ 52.090,00, Ano: 2016{}'''.format(cores['roxo'], '\033[m'))
elif carro == 4:
    print('{}CARREGANDO OS CARROS DISPONIVEIS ......{}'.format(cores['amarelo'], '\033[m'))
    sleep(3)
    print('{}ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:{}'.format(cores['azul2'], '\033[m'))
    print('''{}
[1] - Carro: Argo, Preço: R$ 50.090,00, Ano: 2019
[2] - Carro': Bravo, Preço: R$ 70.000,00, Ano: 2018
[3] - Carro': Mobi, Preço: R$ 48.672,00, Ano: 2019
[4] - Carro': Palio, Preço: R$ 29.800,00, Ano: 2015
[5] - Carro': Siena, Preço: R$ 45.900,00, Ano: 2018
[6] - Carro': Toro, Preço: R$ 83.900,00, Ano: 2017
[7] - Carro': Uno, Preço: R$ 42.900,00, Ano: 2017{}'''.format(cores['roxo'], '\033[m'))
elif carro == 5:
    print('{}CARREGANDO OS CARROS DISPONIVEIS ......{}'.format(cores['amarelo'], '\033[m'))
    sleep(3)
    print('{}ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:{}'.format(cores['azul2'], '\033[m'))
    print('''{}
[1] - Carro: Ka, Preço: R$ 53.000,00, Ano: 2019{}'''.format(cores['roxo'], '\033[m'))
elif carro == 6:
    print('{}CARREGANDO OS CARROS DISPONIVEIS ......{}'.format(cores['amarelo'], '\033[m'))
    sleep(3)
    print('{}ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:{}'.format(cores['azul2'], '\033[m'))
    print('''{}
[1] - Carro: City, Preço: R$ 63.400,00, Ano: 2017
[2] - Carro: Civic, Preço: R$ 124.900,00, Ano: 2018
[3] - Carro: Fit, Preço: R$ 65.050,00, Ano: 2016
[4] - Carro: HR-V, Preço: R$ 91.500,00, Ano: 2016{}'''.format(cores['roxo'], '\033[m'))
elif carro == 7:
    print('{}CARREGANDO OS CARROS DISPONIVEIS ......{}'.format(cores['amarelo'], '\033[m'))
    sleep(3)
    print('{}ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:{}'.format(cores['azul2'], '\033[m'))
    print('''{}
[1] - Carro: Creta, Preço: R$ 77.890,00, Ano: 2019
[2] - Carro: HB20, Preço: R$ 37.990,00, Ano: 2018
[3] - Carro: Ix35, Preço: R$ 98.810,00, Ano: 2019
[4] - Carro: I30, Preço: R$ 38.890,00', Ano: 2019
[5] - Carro: Tucson, Preço: R$ 42.800,00, Ano: 2013{}'''.format(cores['roxo'], '\033[m'))
elif carro == 8:
    print('{}CARREGANDO OS CARROS DISPONIVEIS ......{}'.format(cores['amarelo'], '\033[m'))
    sleep(3)
    print('{}ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:{}'.format(cores['azul2'], '\033[m'))
    print('''{}
[1] - Carro: 208, Preço: R$ 41.000,00, Ano: 2015{}'''.format(cores['roxo'], '\033[m'))
elif carro == 9:
    print('{}CARREGANDO OS CARROS DISPONIVEIS ......{}'.format(cores['amarelo'], '\033[m'))
    sleep(3)
    print('{}ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:{}'.format(cores['azul2'], '\033[m'))
    print('''{}
[1] - Carro: Duster, Preço: R$ 56.900,00, Ano: 2017
[2] - Carro: Kwid, Preço: R$ 29.000,00, Ano: 2018
[3] - Carro: Hilux, Preço: R$ 119.550,00, Ano: 2018
[4] - Carro: Logan, Preço: R$ 44.690,00, Ano: 2018
[5] - Carro: Sandero, Preço: R$ 40.380,00, Ano: 2017
[6] - Carro: Sw4, Preço: R$ 169.700,00, Ano: 2018
[7] - Carro: Yaris, Preço: R$ 74.590,00, Ano: 2018{}'''.format(cores['roxo'], '\033[m'))
elif carro == 10:
    print('{}CARREGANDO OS CARROS DISPONIVEIS ......{}'.format(cores['amarelo'], '\033[m'))
    sleep(3)
    print('{}ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:{}'.format(cores['azul2'], '\033[m'))
    print('''{}
[1] - Carro': Corolla, Preço: R$ 130.990,00, Ano: 2020{}'''.format(cores['roxo'], '\033[m'))
elif carro == 11:
    print('{}CARREGANDO OS CARROS DISPONIVEIS ......{}'.format(cores['amarelo'], '\033[m'))
    sleep(3)
    print('{}ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:{}'.format(cores['azul2'], '\033[m'))
    print('''{}
[1] - Carro: Gol, Preço: R$ 45.737,00, Ano: 2016
[2] - Carro: Golf, Preço: R$ 80.000,00, Ano: 2019
[3] - Carro: Jetta, Preço: R$ 97.900,00, Ano: 2018
[4] - Carro: Nivus, Preço: R$ 110.000,00, Ano: 2016
[5] - Carro: Polo, Preço: R$ 64.636,00, Ano: 2019
[6] - Carro: T-Cross, Preço: R$ 115.000,00, Ano: 2018
[7] - Carro: Virtus, Preço: R$ 73.470,00, Ano: 2018
[8] - Carro: Voyage, Preço: R$ 51.556,00, Ano: 2017{}'''.format(cores['roxo'], '\033[m'))
else:
    print('Opção invalida. Tente novamente')
    sleep(3)