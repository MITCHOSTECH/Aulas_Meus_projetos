'''def lin():
    print('-' * 30)'''


#Programa principal deve ter 2 linhas vazias abaixo ou enter 2x
#1_Etapa
'''lin()
print('   Curso Em Video')
lin()
lin()
print('    APRENDA PYTHON')
lin()
lin()
print('    RICARDO CALIPIMBUTH')
lin()
'''
#2_Etapa Automatiza ou torna dinâmico
'''def titulo(txt):
    #print('-' * 30) => manual nau munda sempre vai ser 30 (--)
    print(f"{'-' * len(txt)}---")#automático conforme numero de letras
    print(txt)
    print(f"{'-' * len(txt)}---")#automático conforme numero de letras


titulo(' CURSO EM VIDEO')
titulo(' PYTHON É MUITO BOM')
titulo(' O DIOGO É O MEU IRMÃO MAIS VELHOS, MAIS É O MAIS BAIXO')'''

# COLOCANDO EM PRÁTICA

# 1_Etapa
'''a = 4
b = 5
s = a + b
print(s) # resumir em soma(4,5)
a = 8
b = 9
s = a + b
print(s) # soma(8,9)
a = 1
b = 2
s = a + b
print(s)# soma(1,2)'''
# Progrma principal
'''def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma {a} + {b} = {s}')


soma(b = 4, a = 5)# Pode altera os números que fica no primeiro ou segundo mudificando os valores a e b
soma(a = 8, 9) # Erro nesse caso se vai identificar ou alterar valores deve alterar tudo não pode identifica um e outro não. (Identificar todos ou Não identicar nenhum assim o python compreeende)
soma(2, 1)
soma(4, 1)'''
#Empacotar parametros em Tuplas imutável
'''def contador(* num):
    # 1_forma
    for valor in num:
        print(f'{valor}', end="")
    print('Fim')
    #2_forma
    #tamanho = len(num)
    #print(f'Recebi os valores {num} e são no total {tamanho} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''
#desempacotamento valores em tuplas:
'''def contador(* num):
    # 1_forma
    s = o
    for c in num:
        s += c
    print('Somando {valores} temos {s}')'''
#Empacotar paramêtro em lista mutável (Empacotamento)
#Ex: funcao que vai dobrar valores: valores = [7,2,5,0,4]; dobrar(valores); print(valores)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)