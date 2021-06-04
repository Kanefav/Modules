import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLE:
    print('O site não está acessível no momento', end='')
else:
    print('O site está acessível no momento', end='')
finally:
    print('.')