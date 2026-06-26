'''for c in range(1,10+1):
    print(c)
print('FIM.')'''
from time import sleep
'''c = 1
while c < 10 + 1:
    print(c)
    c += 1
print('FIM')'''


'''for c in range(1,5):
    n = int(input('Digite um valor?: '))
print('FIM')'''
'''n = 1
while n != 0 : # fleg CONDIÇÃO DE PARADA
    n = int(input('Digite um valor?: '))
print('FIM')'''

'''resposta = 's'
while resposta == 's':
    n = int(input('Digite um valor?: '))
    resposta = str(input('Quer continuar? [S/N]:  ')).lower().strip()
print('FIM')'''

#Soma dos número pares e impares com a condição while utilizando a condição if com intermedário
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor?: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares!')