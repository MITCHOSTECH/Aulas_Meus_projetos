'''numero_extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezasseis','dezassete','Dezoito','Dezanove','Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while 0 <= num <= 20:
        print(f'O número digitado é {numero_extenso[num]}')
        break
    else:
        print('Tente novamente. ',end='')
    break'''
from operator import index

'''
brasil = ('Atlético-MG','Bahia','Botafogo','Bragantino','Ceará','Corinthians','Cruzeiro','Flamengo','Fluminense','Fortaleza','Grêmio','Internacional','Juventude','Mirassol','Palmeiras','Santos','São Paulo','Sport','Vasco','Vitória')
print('-=' * 50)
print(f'Os cincos primeiros colocados são: {brasil[:5]}\nOs últimos quatro colocados são: {brasil[-4:]}\nAs listas com time em ordem alfabético sÃo: {sorted(brasil)}\nO time juventude na tabela atual apresenta na posição {brasil.index("Sport")+1}')
print('-=' * 20)'''

'''from random import choices
num = (1,2,3,4,5,6,7,8,9,10)
aleatoria = choices(num, k=5)
maior = max(aleatoria)
menor = min(aleatoria)
print(f'Os 5 número escolhido aleatóiriamente pela tupla são: {aleatoria}')

print(f'O maior número sorteado foi: {maior}')

print(f'O menor número é: {menor}')'''

'''valores = (int(input('Digite o primeiro valor: ')),int(input('Digite o segundo valor: ')),int(input('Digite o terceiro valor: ')),int(input('Digite o quarto valor: ')))

print(f'Você digitou o número: {valores}')
print(f'a) O valor 9 apareceu {valores.count(9)} vezes')'''
'''
for n in valores: #Percorrer toda tupla de n ao valor final que se encontra na tuplas valores
    if n % 2 == 0:
        print(f'Os números pares são: {n}',end='')
print(f'O número 3 aparece pela primeira vez na posição {valores.index(3) + 1}')
'''
# pares = tuple(n for n in valores if n % 2 == 0)
#print(pares) # Gerar números par e colocar numa tupla'''
