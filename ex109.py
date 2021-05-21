from PacoteUteis import Num

valor = float(input('Valor para multiplicar: '))
multiplicador = float(input('Multiplicador: '))
formatado = str(input('Numero formatado? <Sim ou Não>')).lower().strip()
if formatado in 'ssim':
    formatado = True
else:
    formatado = False
print(Num.multiplicarr(valor, multiplicador, formatado))