# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

#Cores
branco = '\033[0;30m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
azul = '\033[0;34m'
roxo = '\033[0;35m'
ciano = '\033[0;36m'
cinza = '\033[0;37m'

#Inicio
print(amarelo)
num = int(input('Digite um número inteiro: '))

print(verde)
print('Escolha uma das bases para conversão')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')

print(amarelo)
base = int(input('Sua opção: '))

if (base == 1):
    binario = bin(num)
    print(num,f'Convertido para BINÁRIO é igual a',binario.replace("0b", ""))
elif (base == 2):
    octa = oct(num)
    print(num,f'Convertido para OCTAL é igual a',octa.replace("0o", ""))
elif (base == 3):
    hexa = hex(num).upper()
    print(num,f'Convertido para HEXADECIMAL é igual a',hexa.replace("0X", ""))
else:
    print(vermelho, 'ESTE NÂO É UM VALOR VALIDO')

print(cinza)
