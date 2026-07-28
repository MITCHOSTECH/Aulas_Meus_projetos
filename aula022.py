import Aula022Modulo
#from Aula022Modulo import fatoria, dobro, triplo :
# Não é preciso utilizar Aula022Modulo.fatorial ou triplo nem o drobro

#ATENÇÃO: Não é Recomendado pelo PyThon:
# Nesse caso quando existe duas importações de módulos diferentes com o nome identico da função ex.:(dobro)
# O PyThon executa a função do último módulo importado

num = int(input("Digite um valor: "))
fat = Aula022Modulo.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {Aula022Modulo.dobro(num)}")
print(f"O triplo de {num} é {Aula022Modulo.triplo(num)}")