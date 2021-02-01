des = 'Desafio-034 estruturas condicionais'
print ('{}'.format(des))
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = (float(input('Digite seu salário atual: ')))

if salario <= 1250:
    print ('comentarios', salario + (salario * (15 / 100)))
else:
    print ('comentarios', salario + (salario * (10 /100)))
