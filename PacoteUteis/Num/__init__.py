def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

# Funçoes para o Ex 107 


def multiplicar(num):
    num *= 2
    return num


def dividir(num):
    num /= 2
    return num


def somar(num):
    valor = int(input('Valor para somar: '))
    num += valor 
    return num


def subtrair(num):
    valor = int(input('Valor para subtrair: '))
    num -= valor
    return num


def porcentagem(num):
    valor = int(input('Valor da porcentagem: '))
    num -= num * valor/100
    return num


def moeda(moeda):
    return f'{moeda:6.2f}' 
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