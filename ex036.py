#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

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
print(azul)
casa = float(input('Qual o valor da casa? R$'))               #Valor da casa
salario = float(input('Qual o seu salario? R$'))              #Salario da pessoa
anos = int(input('Em quantos anos você pretende pagar? '))  #Tempo do pagamento

#Descobrindo o valor das parcelas
meses = anos * 12
parcelas = casa / meses

if (parcelas > salario * 0.30):
    print(amarelo, f'\nPara pagar uma casa de R${casa} em {anos} anos a prestação sera de {parcelas}. Empréstimo', vermelho, 'NEGADO!')
    print(cinza)
else:
    print(amarelo, f'\nPara pagar uma casa de R${casa} em {anos} anos a prestação sera de {parcelas}. Empréstimo', verde, 'CONCEDIDO!')
    print(cinza)

