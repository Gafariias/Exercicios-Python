#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

#cores
branco = '\033[0;30m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
azul = '\033[0;34m'
roxo = '\033[0;35m'
ciano = '\033[0;36m'
cinza = '\033[0;37m'

#inicio
n = 0
cont = 0
print(amarelo)
for c in range (1, 501, 2):
    if (c % 3 == 0):
        cont = cont + 1
        n = n + c
        
print(f'A soma de todos os {cont} valores é igual a {n}')
print(cinza)