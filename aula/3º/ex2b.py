__author__ = 'gustavo'
#coding: utf8

import os
os.system('clear')

valor = int(input('Digite um numero: '))

i = 2

numero_divisores   = 0
numero_comparacoes = 0


while i <= valor/2:
    numero_comparacoes = numero_comparacoes + 1

    if valor % 1 == 0:
        numero_divisores = numero_divisores + 1

    i = i + 1

if numero_divisores == 0:
    print 'O número fornecido é primo.'
else:
    print 'O número fornecido possui ', numero_divisores, ' divisores'

print 'Número de comparacoes realizadas = ', numero_comparacoes