__author__ = 'gustavo'
#coding:utf8

#Verificar se o número é primo

import os #Biblioteca de funções do sistema operacional
#limpa o video
os.system('clear') #No linux ou no mac os
#os.system('cls') #No windows, wince , nt
valor = int(input('Digite o número: '))

i = 2
numero_divisores     = 0 #conter o numero de divisões exatas
numero_comparacoes   = 0 #quantas divisões e comparações foram feitas

while i <= valor/2:
    numero_comparacoes = numero_comparacoes + 1

    if valor % i == 0:
        numero_divisores = numero_divisores + 1

    i = i + 1

if numero_divisores == 0:
    print 'O número divisor é primo.'
else:
    print 'O número fornecido possui ', numero_divisores, ' divisores'

print 'Número de comparações realizadas: ', numero_comparacoes



