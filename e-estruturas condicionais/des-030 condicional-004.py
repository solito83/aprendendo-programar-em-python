des = 'Desafio-030 estruturas condicionais'
print ('{}'.format(des))
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número: '))
n1 = num % 2
if n1 == 0:
    print ('Esse número é par')
else:
    print ('Esse número é ímpar')
