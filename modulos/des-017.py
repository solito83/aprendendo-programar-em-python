des = 'Pitagoras: medidas de um triângulo'
print ('{}'.format(des))
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

caop = int(input('Digito: '))
caad = int(input('Digito: '))
hipo = caop ** 2 + caad ** 2
fim = 'The End'

print ('O cateto oposto é: {} unid.medida\nO cateto adjacente é: {} unid.medida\nA hipotenusa vale: {:.2f} unid.medida\n{}'.format(caop, caad, hipo ** (1 / 2), fim))

#from math import pow
