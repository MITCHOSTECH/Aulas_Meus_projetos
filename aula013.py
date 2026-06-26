
#for c in range(6,0,-1): #Contar de tras para frente
'''for c in range(6,0,-1):
    print(c)
print('fim')
i = int(input('Inicio?: '))
f = int(input('Fim?: '))
p = int(input('Passo'))
for c in range(i,f+1,p):#inicio é começo da numeração, Fim é fim da numeração,passo é passos dado pelos números por exemplo 1 uma casa 2 pular duas em duas casa sucessivamente
    print(c)
print('Fim')'''
s = 0
for c in range(0,4):
    n = int(input('Digite um valor?: '))
    s += n       # pode ser assim no python (s = s + n)
print(f'o somatório de todos os valores  foi: {s}')
