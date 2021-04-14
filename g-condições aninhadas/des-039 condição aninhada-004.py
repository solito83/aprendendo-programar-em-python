des = 'Desafio-39 condições aninhadas-004'
print ('{}'.format(des))
'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu: '))
idade = atual - nasc
print ('Você nasceu em {} e tem {} anos.'.format(nasc, idade))
if idade == 18:
    print ('Você tem que se alistar imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    if saldo == 1:
        print ('Ainda faltam {} ano para você se alistar.'.format(saldo))
    else:
        print ('Ainda faltam {} anos para você se alistar.'.format(saldo))
    ano = atual + saldo
    print ('Seu alistamento será em {}.'.format(ano))    
elif idade > 18:
    saldo = idade - 18
    if saldo == 1:
        print ('Você deveria ter se alistado há {} ano.'.format(saldo))
    else:
        print ('Você deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print ('Seu alistamento foi em {}.'.format(ano))
print ('The End!!!')
