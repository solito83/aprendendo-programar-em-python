des = 'Desafio-036 estrutura condição aninhada-001'
print ('{}'.format(des))
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa a ser comprada: '))
sala = float(input('Digite o salario do comprador: '))
temp = int(input('Digite em quantos anos deseja quitar sua casa: '))
pres = casa / (temp*12)

'''
maximo = sala * (30/100)
if pres <= maximo:
    print ('Emprestimo concedido')
else:
    print ('Emprestimo negado')
'''

print ('O valor da prestação é de: R${:.2f} reais'.format(pres))

if casa / (temp*12) <= (sala * (30/100)):
    print ('\033[0;31mParabéns!!! você está Pronto para se mudar?\033[m')

elif  casa / (temp*12) > (sala * (30/100)) and casa / (temp*12) < (sala * (40/100)) :
    print ('\033[0;32m!!!Podemos tentar uma casa mais em conta.\033[m')

else:
    print ('\033[4;35mSinto muito você não pode comprar esta casa!\033[m')
