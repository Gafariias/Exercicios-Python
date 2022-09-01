#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

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
num2 = int(input('Digite outro número inteiro: '))

print(verde)
if (num > num2):
    print(f'O número {num} é maior.')
elif (num2 > num):
    print(f'O número {num2} é maior.')
else:
    print('Os dois valores são iguais.')

print(cinza)

