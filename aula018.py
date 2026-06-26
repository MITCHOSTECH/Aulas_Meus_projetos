'''teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)'''

# declarar galera
'''
galera = [['João', 19],['Ana', 33],['Jooquim', 13],['Maria', 45]]
    #print(galera[0][0][0:1]) # imprimir as posições
for p in galera:
    print(f"{p[0]} tem  {p[1]} anos de idade.")
'''
# pedir nome e idade
totmai = totmen = 0
galera = list() # É a primeira lista
dado = list() # lista secundária que vai recuperar todos os dados
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

# Verificar pessoas com mais de 21 anos
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maior e {totmen } menor de idade.')