des = 'Sen, cosseno e tangente de um ângulo'
print ('{}'.format(des))
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print ('O angulo de = {} tem o seno = {:.2f}'.format(ang, seno))
print ('O angulo de = {} tem o cosseno = {:.2f}'.format(ang, coss))
print ('O angulo de = {} tem a tangente = {:.2f}'.format(ang, tang))

print('The End')
