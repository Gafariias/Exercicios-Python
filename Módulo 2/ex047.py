#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

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
print(amarelo)
for c in range(2, 51, 2):
    print(c, end=' ')
print(roxo, end=' ')
print('ACABOU')
print(cinza)