n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
ss = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a subtração é {}, o produto é {} \n e a divisão é {:.3f}'.format(s, ss, m, d), end=' ')
print('a divisão inteira {} e a potência {}'.format(di, e))


