pessoas = {'nome': 'Ricardo', 'sexo': 'M', 'idade': 22}
'''print( f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(f'{pessoas.keys()}')
print(f'{pessoas.values()}')#Mostrando Items'''


# Iterar o dicionário
'''for k, v in pessoas.items():
    print(f'{k} = {v}')'''

# Criar dicionário dentro de uma lista
'''brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'Sigal': 'R'}
estado2 = {'uf': 'São Paulo', 'Sigal': 'S'}
brasil.append(estado1)
brasil.append(estado2)

#fatiamento dicionário
print(brasil[1]['uf'])'''

# Importante Atenção
estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigal'] = str(input('Sigal do estado: '))
    brasil.append(estado.copy())
#Normal
# print(brasil)

# Melhor
for e in brasil:
    # Iterar chaves e valores
    #for k, v in e.items():
        #print(f'O campo {k} te valor {v}')
    # Iterar valores
    for v in e.values():
        print(f'{v}', end=' ')
    print()