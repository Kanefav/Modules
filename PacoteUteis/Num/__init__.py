def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

# Funçoes para o Ex 107 


def multiplicar(num, format=False):
    num *= 2
    return num if format == False else moeda(num)


def dividir(num, format=False):
    num /= 2
    return num if format == False else moeda(num)


def somar(num, info=False):
    if info == False:
        valor = int(input('Valor para somar: '))
        num += valor 
        return num
    else:
        valor = float(input('Valor para somar: '))
        num += valor
        lista = [moeda(num), moeda(valor)]
        return lista


def subtrair(num, info=False):
    if info == False:
        valor = int(input('Valor para subtrair: '))
        num -= valor
        return num
    else:
        valor = float(input('Valor para subtrair: '))
        num -= num
        lista = [moeda(num), moeda(valor)]
        return lista

def porcentagem(num):
    valor = int(input('Valor da porcentagem: '))
    num -= num * valor/100
    return num


def moeda(moeda):
    return f'{moeda:5.2f}' 
    # O primeiro numero 5, é o total de caracteres que são formatados 
    # para ficar no mesmo nível, exemplo (ex108.py)


def elevado(num, VezesElevadas):
    resultado = 0
    numero = num
    for c in range(0, VezesElevadas - 1):
       resultado = num * numero
       num = resultado
    return resultado


# função para o ex 109 
# ela devolve a valor formatado dependendo do que for mandado
def multiplicarr(valor, multiplicador, format=False):
    valor = valor * multiplicador
    return valor if format is False else moeda(valor)


def resumo(valor):
    SomaTemp = somar(valor, True)
    SubtracaoTemp = subtrair(valor, True)
    print('/-/'*6)

    print('       Resumo de Valores')
    print(f'A multiplicação de {valor} por 2 é {multiplicar(valor, True)}')
    print(f'A divisão de {valor} por 2 é {dividir(valor, True)}')
    print(f'O valor de {moeda(valor)} + {SomaTemp[1]} é igual a {SomaTemp[0]}')
    print(f'O valor de {moeda(valor)} - {SubtracaoTemp[1]} é igual a {SubtracaoTemp[0]}')

    print('/-/'*6)