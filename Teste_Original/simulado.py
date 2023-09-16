from time import sleep

cor6 = {'azul':'\033[0:34m',
        'amarelo':'\033[1:33m',
        'roxo':'\033[1:35m',
        'azul2':'\033[1:34m'}

opcao = 0
while opcao != 1:
    print('{}PODEMOS DAR INICIO AO SIMULADO?{} '.format(cor6['azul2'], '\033[m'))
    print('{}[1] - Podemos sim, Claro!{}'.format(cor6['roxo'], '\033[m'))
    opcao = int(input('{}Qual é a sua escolha:{} '.format(cor6['amarelo'], '\033[m')))
    if opcao == 1:
        print('Maravilha, vamos continuar.')
        break
        sleep(1)
    else:
        print('{}Opção invalida. Tente novamente{}'.format(cor6['azul2'], '\033[m'))

Valor = int(input('{}VALOR DO VEICULO DE ACORDO COM A TABELA QUE MANDEI ACIMA:{} '.format(cor6['roxo'], '\033[m')))
sleep(1)

Qtd = int(input('{}QUANTIDADE DE VEICULO QUE O SR(a) DESEJA COMPRAR:{} '.format(cor6['roxo'], '\033[m')))
sleep(1)

Entrada = int(input('{}VALOR QUE O SR(a) PRETENDE DAR DE ENTRADA:{} '.format(cor6['roxo'], '\033[m')))
sleep(1)

Parcela = int(input('{}DE 2 a 96 PARCELAS O SR(a) PRETENDE FINANCIAR EM QUANTAS VEZES?:{} '.format(cor6['roxo'], '\033[m')))
sleep(1)
print('{}ESTAMOS FAZENDO O CALCULO, AGUARDE POR FAVOR.........{}'.format(cor6['amarelo'], '\033[m'))
sleep(3)

if Parcela <= 32:
    total_com_juros = Valor * Qtd * 0.10
    print('{}Pela quantidade de parcelas escolhida, o juros sera de 10%{}'.format(cor6['azul2'], '\033[m'))
elif Parcela > 33 and Parcela <= 64 :
    total_com_juros = Valor * Qtd * 0.15
    print('{}Pela quantidade de parcelas escolhida, o juros sera de 15%{}'.format(cor6['azul2'], '\033[m'))
else:
    total_com_juros = Valor * Qtd * 0.35
    print('{}Pela quantidade de parcelas escolhida, o juros sera de 35%{}'.format(cor6['azul2'], '\033[m'))
Total = Valor + total_com_juros
Desconto = Total - Entrada
Parcelas = Desconto / Parcela

print('{}PREÇO SEM DESCONTO{} {}R${:.2f}{}'.format('\033[1:34m', '\033[m', cor6['amarelo'], Total, '\033[m'))
sleep(1)

print('{}PREÇO COM O DESCONTO DA ENTRADA{} {}R${:.2f}{}'.format('\033[1:34m', '\033[m', cor6['amarelo'],Desconto, '\033[m'))
sleep(1)

print('{}O VALOR DAS PARCELAS SERA DE{} {}R${:.2f} mensais{}'.format('\033[1:34m', '\033[m', cor6['amarelo'], Parcelas, '\033[m'))
sleep(1)

opcao = 0
while opcao != 2:
    print('{}PODEMOS DAR INICIO A APROVAÇÃO?{} '.format(cor6['amarelo'], '\033[m'))
    print('''{}
[1] - Podemos sim, claro!
[2] - Eu gostaria de refazer simulado{}'''.format(cor6['roxo'], '\033[m'))
    opcao = int(input('{}Qual é a sua escolha:{} '.format(cor6['amarelo'], '\033[m')))
    if opcao == 1:
        print('Maravilha, então vamos continuar.')
        break
        sleep(2)
    elif opcao == 2:
        print('Perfeito, vamos iniciar novamente então.')
        Valor = int(
            input('{}VALOR DO VEICULO DE ACORDO COM A TABELA QUE MANDEI ACIMA:{} '.format(cor6['roxo'], '\033[m')))
        sleep(1)

        Qtd = int(input('{}QUANTIDADE DE VEICULO QUE O SR(a) DESEJA COMPRAR:{} '.format(cor6['roxo'], '\033[m')))
        sleep(1)

        Entrada = int(input('{}VALOR QUE O SR(a) PRETENDE DAR DE ENTRADA:{} '.format(cor6['roxo'], '\033[m')))
        sleep(1)

        Parcela = int(input(
            '{}DE 2 a 96 PARCELAS O SR(a) PRETENDE FINANCIAR EM QUANTAS VEZES?:{} '.format(cor6['roxo'], '\033[m')))
        sleep(1)
        print('{}ESTAMOS FAZENDO O CALCULO, AGUARDE POR FAVOR.........{}'.format(cor6['amarelo'], '\033[m'))
        sleep(3)

        if Parcela <= 32:
            total_com_juros = Valor * Qtd * 0.10
            print('{}Pela quantidade de parcelas escolhida, o juros sera de 10%{}'.format(cor6['azul2'], '\033[m'))
        elif Parcela > 33 and Parcela <= 64:
            total_com_juros = Valor * Qtd * 0.15
            print('{}Pela quantidade de parcelas escolhida, o juros sera de 15%{}'.format(cor6['azul2'], '\033[m'))
        else:
            total_com_juros = Valor * Qtd * 0.35
            print('{}Pela quantidade de parcelas escolhida, o juros sera de 35%{}'.format(cor6['azul2'], '\033[m'))
        Total = Valor + total_com_juros
        Desconto = Total - Entrada
        Parcelas = Desconto / Parcela
        sleep(1)

        print('{}PREÇO SEM DESCONTO{} {}R${:.2f}{}'.format('\033[1:34m', '\033[m', cor6['amarelo'], Total, '\033[m'))
        sleep(1)

        print('{}PREÇO COM O DESCONTO DA ENTRADA{} {}R${:.2f}{}'.format('\033[1:34m', '\033[m', cor6['amarelo'], Desconto, '\033[m'))
        sleep(1)

        print('{}O VALOR DAS PARCELAS SERA DE{} {}R${:.2f} mensais{}'.format('\033[1:34m', '\033[m', cor6['amarelo'], Parcelas, '\033[m'))

        sleep(2)
    else:
        print('Opção invalida. Tente novamente')
        sleep(2)
opcao = 0
while opcao != 1:
    print('{}O SR(a) APROVA O VALOR SOLICITADO?:{} '.format(cor6['amarelo'], '\033[m'))
    print('{}[1] - SIM'.format(cor6['roxo'], '\033[m'))
    opcao = int(input('{}OPÇÃO:{} '.format(cor6['amarelo'], '\033[m')))
    if opcao == 1:
        print('{}Perfeito!{}'.format(cor6['azul2'], '\033[m'))
    #elif opcao == 2:
        #print('{}Ok! Entao vamos iniciar novamente o simulado:{}'.format(cor6['azul'], '\033[m'))
    else:
        print('{}Opção invalida. Tente novamente{}'.format(cor6['azul2'], '\033[m'))
sleep(2)

opcao = 0
while opcao != 2:
    print('{}SENDO ASSIM VAMOS DAR INICIO AO PROCESSO DE APROVAÇÃO?:{} '.format(cor6['amarelo'], '\033[m'))
    print('''{}
[1] - OPA! Vamos sim claro.{}'''.format(cor6['roxo'], '\033[m'))
    opcao = int(input('{}OPÇÃO:{} '.format(cor6['amarelo'], '\033[m')))
    if opcao == 1:
        break
    else:
        print('{}Opção invalida. Tente novamente{}'.format(cor6['azul2'], '\033[m'))
sleep(2)
valor = float(input('{}DIGITE O VALOR DO VEICULO COM DESCONTO: R${}'.format(cor6['roxo'], '\033[m')))
salario = float(input('{}DIGITE O VALOR DO SEU SALARIO: R${}'.format(cor6['roxo'], '\033[m')))
parcelas = int(input('{}EM QUANTAS VEZES O SR(a) DESEJA FINANCIAR:{} '.format(cor6['roxo'], '\033[m')))
preco = valor / parcelas
minimo = salario * 30 / 100

sleep(1)
print('{}AGUARDE, ESTAMOS ANALISANDO ......{}'.format(cor6['amarelo'], '\033[m'))
sleep(5)

print('{}PARA PAGAR UM CARRO DE R${:.2f} EM {}x, A PRESTAÇÃO SERA DE R${:.2f} E O SR(a) GANHA R${:.2f}.{}'.format(cor6['azul2'], valor, parcelas, preco, salario, '\033[m'))
if preco <= minimo:
    print('{}DESTA FORMA O PEDIDO DO SR(a) FOI APROVADO, MEUS PARABENS!!{}'.format(cor6['roxo'], '\033[m'))
    from dialogo import cor7
else:
    print('{}DESTA FORMA O PEDIDO DO SR(a) INFELIZMENTE NÃO FOI APROVADO, SINTO MUITO POR ISSO.{}'.format(cor6['roxo'], '\033[m'))
    from dialogo2 import cor8



