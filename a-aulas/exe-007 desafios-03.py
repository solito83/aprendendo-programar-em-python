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

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
ex = n1**n2
re = n1%n2

print('A soma é: {}; o produto é: {}; e a divisão é: {:.3f}'.format(s, m, d))
# Na divisão, para indicar o número de casas decimais podemos fazer da seguinte forma {:.2f} {:}=tag 2=o numero de casas decimais desejadas e f=float->flutuante.
print('A divisão inteira é:{}; \nO expoente é:{}; \nO resto da divisão é:{};'.format(di, ex, re))
# "\n = quebrar linha"
# " end='' =continuar escrevendo na mesma linha".

fim = ('The End.')
print('{:^12}!'.format(fim))