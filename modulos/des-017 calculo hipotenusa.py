des = 'Pitagoras: medidas de um triângulo'
print ('{}'.format(des))
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

from math import hypot
co = float(input('Digito: '))
ca = float(input('Digito: '))
fim = 'The End'

#{1ª forma}
#hi = (co ** 2 + ca ** 2) ** (1 / 2)
#print ('O cateto oposto é: {} unid.medida\nO cateto adjacente é: {} unid.medida\nA hipotenusa vale: {:.2f} unid.medida\n{}'.format(co, ca, hi , fim))

#{2ª forma}
hi = hypot(co, ca)
print ('A hipotenusa vale {:.2f} unid.madida\n{}'.format(hi, fim))
