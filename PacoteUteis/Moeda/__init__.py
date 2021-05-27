from PacoteUteis import Num


def ValidarMoeda(moeda):
    valido = False
    while valido is not True:
        string = str(input(moeda)).replace(",", ".").replace(" ", "")
        if string.isalpha() or string == '':
            print(f'Erro: "{string}" não é um numero válido')
        else:
            valido = True
            return float(string)