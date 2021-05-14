from time import sleep
from PacoteUteis import Num
preco = int(input('Preço Inicial: '))
while True:
    precoatl = str(input('Alguma alteração a se fazer? [S/N]')).lower()
    if precoatl in 'ssim':
        print('''Você pode dividir ou multiplicar o valor por 2, somar e subtrair,
        Pode também tirar porcentagem \n
                Digite 1 para Multiplicar 
                       2 para dividir 
                       3 para somar
                       4 para subtrair
                       5 para tirar porcentagem
        ''')
        opcao = int(input('Escolha: '))
        if opcao == 1:
            print('Multiplicando...')
            sleep(1)
            print(f'O dobro de {preco} é {Num.multiplicar(preco)}')
            preco = Num.multiplicar(preco)
        if opcao == 2:
            print('Dividindo...')
            sleep(1)
            print(f'A metade de {preco} é {Num.dividir(preco)}')
            preco = Num.dividir(preco)
        if opcao == 3:
            preco = Num.somar(preco)
            print('Somando...')
            sleep(1)
            print(f'O valor da soma é {preco}')
        if opcao == 4:
            preco = Num.subtrair(preco)
            print('Subtraindo...')
            sleep(1)
            print(f'O valor da subtração é {preco}')
        if opcao == 5:
            preco = Num.porcentagem(preco)
            print('Tirando a porcentagem...')
            sleep(1)
            print(f'O valor foi atualizado para {preco}')
    else:
        break
print(f'O preço final foi {preco}')
print('Programa finalizado.')
