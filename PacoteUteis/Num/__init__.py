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