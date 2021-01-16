des = ('Conversor de metros para centimetros e milimetros')
print ('{}.'.format(des))
#Desafio-08 >>> Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

me = float(input('Digite um número: '))

ce = (me*100)
mi = (me*1000)

print('Você tem {:.0f} metros \nOu {:.0f} centimetros \nOu {:.0f} milimetros'.format(me, ce, mi))

print('The End')
