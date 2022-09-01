#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#função
from time import sleep as s

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
print(roxo)
for c in range (10, -1, -1):
    print(c)
    s(1)

print(amarelo)
print('BUMM! BUMM! POWWW!')
print('FELIZ ANO NOVO')
print(cinza)