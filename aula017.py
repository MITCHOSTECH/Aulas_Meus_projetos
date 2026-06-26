'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7) # Adicionar valores
num.sort(reverse=True) # Sort => ordenar valores. reverse = True => Desordenar
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print(f'O número quatro não encontrado!')
print(num)
print(f"ESta lista tem {len(num)} {'elemento' if len(num) <= 1 else 'elementos' }")'''

# CRIAÇÃO DE  LISTA VAZIO E ADICIONAR VALORES
# IMPRIMINDO DE MANEIRAS DIFERENTES
'''valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores: # Emprimir valores uzando for
    print(f'{v}...')
for pos, v in enumerate(valores):
    print(f"Na posição {pos +1} tem o valor {v}...")
print(valores)'''

# CRIAÇÃO DE LISTA VAZIO
# UTILIZANDO O CICLO FOR PARA INTRODUZIR 5 VALORES DENTRO DA LISTA VÁZIA
'''valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont + 1} valor: ')))
for pos, v in enumerate(valores):
    print(f'Na posição {pos + 1} encontrei o valor {v}!')'''

a = [2, 3, 4, 7]
#b = a # ERRADO! ISSO NÃO É UMA COPIA DA LISTA MAIS SIM JUNÇÃO DA LISTA A e B
#b = a[:] # CERTO
b = a.copy() # CERTO
b[2] = [8]
print(f'Lista A: {a}')
print(f'Lista B: {b}')

