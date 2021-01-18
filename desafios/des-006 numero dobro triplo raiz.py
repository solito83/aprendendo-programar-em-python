des = ('Desafio-006 número dobro triplo raiz')
print ('{}.'.format(des))
#Desafio-06 >>> Crie um programa que leia um número e mostre o seu dobro, seu triplo e sua rais quadrada.

n1 = int(input('Digite um número: '))
do = n1*2
tr = n1*3
rz = n1**(1/2)
print ('O dobro do número que você digitou é {}. \nE seu triplo é {}. \nJá sua raiz é {:.2f}.'.format(do, tr, rz))

print ('The End')