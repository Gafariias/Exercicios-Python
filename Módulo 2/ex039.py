#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#cores
branco = '\033[0;30m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
azul = '\033[0;34m'
roxo = '\033[0;35m'
ciano = '\033[0;36m'
cinza = '\033[0;37m'

#chamando módulos
from datetime import date

#inicio
print(amarelo)
ano = int(input('Ano de nascimento: '))
anoatual = date.today()
anoatual = anoatual.year
idade = anoatual - ano

print(verde)
print(f'Você possui ou vai fazer {idade} anos de idade')
if (idade > 18):
    temporestante = idade - 18
    print(f'Ja se passaram {temporestante} anos desde seu alistamento')
    print(f'Seu alistamento foi em {anoatual - temporestante}')
elif (idade < 18):
    temporestante = (idade - 18) * -1
    print(f'Ainda falta {temporestante} anos para seu alistamento')
    print(f'Seu alistamento sera em {anoatual + temporestante}')
else:
    print('Seu alistamento é este ano')

print(cinza)