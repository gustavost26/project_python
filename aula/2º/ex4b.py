__author__ = 'gustavo'

#Programa para calcular a hipotenusa de um triangulo retangulo.

import math

a = int(input('Digite um valor para o lado A: '))
b = int(input('Digite um valor para o lado B: '))
h = math.sqrt(a * a + b * b)
print 'Hipotenusa = ', h

