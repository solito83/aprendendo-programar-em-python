des = 'Aluguel de carro'
print ('{}'.format(des))
#Desafio-015 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int(input('Quantos dias você ficou com o veiculo? '))
km = float(input('Quantos Km você rodou? '))

pago = dia * 60 + km * 0.15
fim = 'The End'

print ('O total a pagar é de R${:.2f} reais\n{}'.format(pago,fim))
