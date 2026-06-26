n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
a = n1 + n2
m = n1 * n2
d = n1 / n2
s = n1 - n2
di = n1 // n2
e = n1 ** n2
print('A soms é {},\n o produto é {}, subtracao é {}, e a  \n divisão é {:.3f}'.format(a, m, s, d), end='>>>>')
print('Divisão inteira {}'.format(di, e))
