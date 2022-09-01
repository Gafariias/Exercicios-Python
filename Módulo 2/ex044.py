#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

#Cores
from ssl import VERIFY_DEFAULT


branco = '\033[0;30m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
azul = '\033[0;34m'
roxo = '\033[0;35m'
ciano = '\033[0;36m'
cinza = '\033[0;37m'

#inicio
print(ciano)
valor = float(input('Digite o valor do produto: '))

print(verde)
print(verde,f'FORMA DE PAGAMENTO')
print(amarelo)
print('[1] à vista no dinheiro/cheque')
print('[2] à vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
print(verde)
op = int(input('Qual sua opção? '))

if (op == 1):
    print(f'Sua compra de R${valor} vai custar {valor - (valor * 0.10):.2f} no final')
elif (op == 2):
    print(f'Sua compra no valor de {valor} vai custar {valor - (valor * 0.05):.2f} no final')
elif (op == 3):
    print(f'sua compra sera parcelada em 2X de {valor / 2}')
    print(f'Sua compra no valor de {valor} vai custar {valor} no final')
elif (op == 4):
    par = int(input('Quantas parcelas? '))
    juros = valor + (valor * 0.20)
    print(f'Sua compra sera parcelada em {par}X de {juros / par} COM JUROS')
    print(f'Sua compra no valor de {valor} vai custar {valor + (valor * 0.20):.2f} no final')
else:
    print('POR FAVOR, INSIRA UM VALOR VALIDO')

print(cinza)