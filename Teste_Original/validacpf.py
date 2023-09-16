from time import sleep
cor4 = {'azul':'\033[0:34m',
        'amarelo':'\033[1:33m',
        'roxo':'\033[1:35m',
        'azul2':'\033[1:34m'}

def NumerarCPF():
    for a in cpf:
        a = int(a)
        cpf_numerado.append(a)

def quantidade():
    if len(cpf) < 11 or len(cpf) > 11:
        return False
    else:
        return True

def primeiro_digito():
    if len(cpf_numerado) < 11 or len(cpf_numerado) > 11:
        return False
    else:
        acumulador = 0
        resultado = 0
        controlador = 10
        for numeros in cpf_numerado[0:9]:
            resultado = numeros * controlador
            acumulador += resultado
            controlador = controlador - 1
        acumulador = acumulador * 10 % 11
        if acumulador == 10:
            acumulador = 0
        if acumulador == cpf_numerado[9]:
            return True
        else:
            return False

def segundo_digito():
    if len(cpf_numerado) < 11 or len(cpf_numerado) > 11:
        return False
    else:
        acumulador2 = 0
        resultado2 = 0
        controlador2 = 11
        for numeros2 in cpf_numerado[0:10]:
            resultado2 = numeros2 * controlador2
            acumulador2 += resultado2
            controlador2 = controlador2 - 1
        acumulador2 = acumulador2 * 10 % 11
        if acumulador2 == 10:
            acumulador2 = 0
        if acumulador2 == cpf_numerado[10]:
            return True
        else:
            return False

sleep(1)
cpf_numerado = []
cpf = str(input('{}DIGITE O SEU CPF{}: '.format(cor4['azul2'], '\033[m'))).replace('.', '').replace('-', '')

print('{}ANALISANDO ........{}'.format(cor4['amarelo'], '\033[m'))
sleep(3)

NumerarCPF()

quantidade()

primeiro_digito()

segundo_digito()

if quantidade() == True and primeiro_digito() == True and segundo_digito() == True:
    print("{}Maravilha, o seu CPF é válido{}".format(cor4['azul2'], '\033[m'))
    sleep(1)
else:
    print("{}Poxa que pena, infelizmente seu CPF não é válido.{}".format(cor4['azul2'], '\033[m'))
    sleep(1)