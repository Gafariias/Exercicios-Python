#Crie um programa que faça o computador jogar Jokenpô com você.

#Modulos
import random

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
print('Vamos jogar Pedra, Papel e Tesoura')
op = ['Pedra', 'Papel', 'Tesoura']
op = random.choice(op)

print(verde)
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
me = int(input('Qual a sua escolha? '))
print(amarelo)
print(f'Eu escolho {op}')

#jogo
if (me == 1) and (op == 'Pedra'):
    print(roxo,'EMPATE')
elif (me == 2) and (op == 'Papel'):
    print(roxo,'EMPATE')
elif (me == 3) and (op == 'Tesoura'):
    print(roxo,'EMPATE')
elif (me == 1) and (op == 'Tesoura'):
    print(verde,'VOCÊ GANHOU!')
elif (me == 2) and (op == 'Pedra'):
    print(verde,'VOCÊ GANHOU!')
elif (me == 3) and (op == 'Papel'):
    print(verde,'VOCÊ GANHOU!')
elif (me != 1) and (me != 2) and (me != 3):
    print(vermelho,'ESCOLHA UM NUMERO VALIDO')
else:
    print(vermelho,'VOCÊ PERDEU!')

print(cinza)
