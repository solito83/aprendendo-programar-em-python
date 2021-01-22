des = 'Conversor de temperaturas "Celcius" para "fahrenheit"'
print ('{}'.format(des))
#Desafio-014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Qual é a temperatura agora? '))

fah = cel * (9/5) + 32
fim = 'The End'

print ('A temperatura em "Celsius" agora é {:.1f}°C\nLogo a temperatura em fahrenheit é {:.1f}°F\n{}'.format(cel,fah,fim))
