des = 'Desafio-035 estruturas condicionais'
print ('{}'.format(des))
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

s1 = float(input('Digite o primeiro seguimento: '))
s2 = float(input('Digite o segundo seguimento: '))
s3 = float(input('Digite o terceiro seguimento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print ('\033[0;32mUuuuual você tem um triângulo\033[m')
else:
    print ('\033[0;31mOooopss você não tem um triângulo\033[m')
    