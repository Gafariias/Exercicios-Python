#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

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
l1 = int(input('Qual o valor do primeiro segmento? '))
l2 = int(input('Qual o valor do segundo segmento? '))
l3 = int(input('Qual o valor do terceiro segmento? '))

print(verde)
if (l1 + l2 > l3) or (l1 + l3 > l2) or (l3 + l2 > l1):
    print(roxo, f'Isso não é um triangulo')
elif (l1 == l2) and (l1 == l3):
    print('Isto é um triangulo EQUILATERO.')
elif (l1 == l2 or l2 == l3 or l1 == l3):
    print('Isto é um triangulo ISÓSCELES.')
elif (l1 != l2) and (l1 != l3) and (l2 != l3):
    print('Isto é um triangulo ESCALENO.')

print(cinza)
