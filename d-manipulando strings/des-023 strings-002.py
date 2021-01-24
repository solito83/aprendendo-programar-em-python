des = 'Desafio-023 strings-002'
print ('{}'.format(des))

#...Faça um programa que leia um número de 0 a 9999 e mostre na telacada um dos digitos separados. ex: unidade; dezena; centena; milhar

n1 = int(input('Digite um número: '))
num = n1
print ((num[3]), 'unidade')
print ((num[2]), 'dezena')
print ((num[1]), 'centena')
print ((num[0]), 'milhar')
