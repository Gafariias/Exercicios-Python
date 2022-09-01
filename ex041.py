#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR Acima de 25 anos: MASTER

#chamada do módulo
from datetime import date

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
nasc = int(input('Digite o ano de nascimento do atleta: '))
hoje = date.today()
anoatual = hoje.year
idade = anoatual - nasc

print(roxo)
print(f'O atleta possui {idade} anos.')

print(ciano)
if (idade <= 9):
    print('Ele se encaixa na categoria MIRIM')
elif (idade <= 14):
    print('Ele se encaixa na categoria INFANTIL')
elif (idade <= 19):
    print('Ele se encaixa na categoria JÚNIOR')
elif (idade <= 25):
    print('Ele se encaixa na categoria SÊNIOR')
else:
    print('Ele se encaixa na categoria MASTER')

print(cinza)