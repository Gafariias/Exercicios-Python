#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

#cores
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
peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em M: '))
alt = altura**2
imc = peso / alt

print(ciano)
print(f'Seu IMC é igual a {imc:.2f}')

if (imc < 18.5):
    print(roxo,'VOCE ESTA ABAIXO DO PESO!')
elif (imc >= 18.5) and (imc < 25):
    print(verde,'VOCÊ ESTA NO PESO IDEAL')
elif (imc >= 25) and (imc < 30):
    print(amarelo, 'VOCÊ ESTA ACIMA DO PESO.')
elif (imc >= 30) and (imc <40 ):
    print(vermelho, 'VOCÊ ESTA OBESO.')
else:
    print(vermelho,'VOCÊ ESTA COM OBESIDADE MÓRBIDA')

print(cinza)