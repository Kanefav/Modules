from PacoteUteis import Num
num = int(input('Digite o preço: '))
VezesElevadas = int(input('Quantas vezes sera elevado? '))
num = Num.elevado(num, VezesElevadas)
Num.moeda(num)
print(Num.moeda(num))
print(Num.moeda(20.29))