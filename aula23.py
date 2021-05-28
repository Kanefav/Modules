from PacoteUteis import Num 
# Tratamento de Erros e Exceções
#try:
#    a = int(input('Numerador: '))
#    b = int(input('Denominador: '))
#    c = a / b
#except Exception as erro:
#    print(f'O erro foi {erro.__class__}')

# um try é composta de:
#    try:
#    except:
#    else:
#    finally:
# exemplo de um completo

try:
    num = float(input('Escreva um número: '))
except ValueError:
    print('Não escreva um número por extenso!')
    continuar = False
    while continuar is False:
        try:
            num = float(input('Escreva um número: '))
            if True:
                continuar = True
        except ValueError:
            print('Não escreva um número por extenso!')

        # se o problema não for reconhecido
        except Exception as erro:
            print('Deu problema')
            print(erro.__class__)
    print(f'O número digitado foi {num}')

# se o problema não for reconhecido
except Exception as erro:
    print('Deu problema')
    print(erro.__class__)
else:
    print(f'O número digitado foi {num}')
finally:
    print('finally sempre é executado ao final')
