des = 'Desafio-041 condições aninhadas-006'
print ('{}'.format(des))
'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''

idade = int(input('Digite sua idade: '))

if idade < 9:
    print ('Você está na categoria mirim')
elif idade < 14:
    print ('Você está na categoria infantil')
elif idade < 19:
    print ('Você está na categoria júnior')
elif idade < 25:
    print ('Você está na categoria sênior')
else:
    print ('Você esta na categoria master')
    