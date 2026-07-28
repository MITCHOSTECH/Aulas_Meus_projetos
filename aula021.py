'''def funcao():
    n1 = 4
    print(f'N1 Local vale {n1}')




n1 = 2
funcao()
print(f'N1 Global vale {n1}')'''

#2 ex.
'''
def calcular(a = 0, b = 0, c = 0):
    s = a + b + c
    return s


r1 = calcular(int(input(f'Digite 1º número do r1: ')),int(input(f'Digite 2º número do r1: ')), int(input(f'Digite 3º número do r1: ')))
r2 = calcular(int(input(f'Digite 1º número do r2: ')),int(input(f'Digite 2º número do r2: ')), int(input(f'Digite 3º número do r2: ')))
r3 = calcular(int(input(f'Digite 1º número do r3: ')),int(input(f'Digite 2º número do r3: ')), int(input(f'Digite 3º número do r3: ')))

print(f'As somatórias dos números foram: {r1}, {r2}, {r3}')'''

# 3ex.
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
'''n = int(input(f'Digite um número: '))
print(f'O fatórial de {n} é igual a {fatorial(n)}')'''

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2}, {f3}')

#4ex.
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input(f'Digite um número: '))
#print(f'{par(num)}')
if par(num):
    print(f'É par')
else:
    print(f'Não é par')