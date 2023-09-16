from time import sleep

cor3 = {'azul':'\033[0:34m',
        'amarelo':'\033[1:33m',
        'roxo':'\033[1:35m',
        'azul2':'\033[1:34m'}

nome = str(input('{}DIGITE O SEU NOME COMPLETO:{} '.format(cor3['azul2'], '\033[m')))
sleep(2)

'''idade = int(input('{}Digite sua Idade:{} '.format(cor3['roxo'], '\033[m')))
if idade >= 18:
    print('{}Otimo você tem mais de 18 anos,'
          'vou continuar o seu cadastro{}.'.format(cor3['roxo'], '\033[m'))
else:
    print('{}Que pena, você é menor de idade,'
          'teria alguem responsavel pra continuar'
          'o cadastro pelo Sr(a)?{}'.format(cor3['roxo'], '\033[m'))'''
idade = 0
while True:
    idade = int(input('{}DIGITE A SUA IDADE:{} '.format(cor3['azul2'], '\033[m')))
    sleep(2)
    if idade >= 18:
        print('{}Otimo você tem mais de 18 anos,'
              'vou continuar o seu cadastro{}.'.format(cor3['roxo'], '\033[m'))
        break
    else:
        print('{}Que pena, você é menor de idade,'
              'teria alguem responsavel pra continuar'
              'o cadastro pelo Sr(a)?{}'.format(cor3['roxo'], '\033[m'))
        break
sleep(2)

sexo = str(input('{}QUAL SEU GENERO? [M/F]:{} '.format(cor3['azul2'], '\033[m'))).strip().upper()[0]
sleep(2)
while sexo not in 'MmFf':
    sexo = str(input('{}Dados invalidos. Por favor, tente novamente:{} '.format(cor3['roxo'], '\033[m'))).strip().upper()[0]
print('{}Sexo {} resgistrado com sucesso{}'.format(cor3['roxo'], sexo, '\033[m'))
sleep(2)

data = input('{}DIGITE SUA DATA DE NASCIMENTO:{} '.format(cor3['azul2'], '\033[m'))
sleep(2)

nome_da_mae = str(input('{}DIGITE O NOME DA SUA MÃE:{} '.format(cor3['azul2'], '\033[m')))
sleep(2)

nome_do_pai = str(input('{}DIGITE O NOME DO SEU PAI:{} '.format(cor3['azul2'], '\033[m')))
sleep(2)

telefone = input('{}DIGITE UM NUMERO PARA CONTATO DDD:{} '.format(cor3['azul2'], '\033[m'))
sleep(2)

endereço = str(input('{}DIGITE O SEU ENDEREÇO:{} '.format(cor3['azul2'], '\033[m')))
sleep(2)

bairro = str(input('{}DIGITE O NOME DO SEU BAIRRO:{} '.format(cor3['azul2'], '\033[m')))
sleep(2)

N_da_casa = int(input('{}DIGITE O NÚMERO DA SUA CASA:{} '.format(cor3['azul2'], '\033[m')))
sleep(2)

print('{}QUAL A SUA PROFISSÃO:{}'.format(cor3['azul2'], '\033[m'))
sleep(1)
print('{}1 - ADMINISTRAÇÃO{}'.format(cor3['roxo'], '\033[m'))
sleep(1)
print('{}2 - APOSENTADO{}'.format(cor3['roxo'], '\033[m'))
sleep(1)
print('{}3 - ARTES E DESIGN{}'.format(cor3['roxo'], '\033[m'))
sleep(1)
print('{}4 - CIENCIAS BIOLOGICAS E DA TERRA{}'.format(cor3['roxo'], '\033[m'))
sleep(1)
print('{}5 - CIENCIAS SOCIAIS E HUMANAS{}'.format(cor3['roxo'], '\033[m'))
sleep(1)
print('{}6 - COMINICAÇÃO E INFORMAÇÃO{}'.format(cor3['roxo'], '\033[m'))
sleep(1)
print('{}7 - DESEMPREGADO{}'.format(cor3['roxo'], '\033[m'))
sleep(1)
print('{}8 - ENGENHARIA E PRODUÇÃO{}'.format(cor3['roxo'], '\033[m'))
sleep(1)
print('{}9 - SAUDE E BEM ESTAR{}'.format(cor3['roxo'], '\033[m'))
sleep(1)
print('{}10 - SERVIDOR PUBLICO{}'.format(cor3['roxo'], '\033[m'))
sleep(1)
print('{}11 - TECNOLOGIA DA INFORMAÇÃO{}'.format(cor3['roxo'], '\033[m'))
sleep(1)
print('{}12 - OUTROS{}'.format(cor3['roxo'], '\033[m'))
sleep(1)

Profissao = int(input('{}Digite a opção desejada:{} '.format(cor3['amarelo'], '\033[m')))

if Profissao > 1 <= 12:
    print('{}MARAVILHA VAMOS CONTINUAR ......{}'.format(cor3['amarelo'], '\033[m'))
    sleep(1)
else:
    print('Opção invalida. Tente novamente')