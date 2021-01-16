print(5+3*2)
print(5**2)
print(5**3)
print(19//2)
print(19/2)
print(25**17)
print(31%3)
print(56**(4/2))
print(25**(1/2))

print('oi'*6)
print('='*12)

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número'))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
ex = n1**n2
re = n1%n2

print('A soma é: {}; o produto é: {}; e a divisão é: {}'.format(s, m, d))

print('A divisão inteira é:{}; O expoente é:{}; o resto da divisão é:{};'.format(di, ex, re))

fim = ('The End.')
print('{:^12}'.format(fim))