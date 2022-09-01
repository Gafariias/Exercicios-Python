#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

#Cores
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
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
med = (n1 + n2) / 2

print(ciano)
print(f'Tirando {n1} e {n2}, a média é do aluno é de {med}')
if (med <5.0):
    
    print(f'O aluno esta {roxo}REPROVADO')
elif (med >= 5 and med < 7):
    print(f'O aluno esta de {amarelo}RECUPERAÇÂO ')
else:
    print(f'O aluno esta {verde}APROVADO')

print(cinza)