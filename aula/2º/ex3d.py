__author__ = 'gustavo'
#coding:utf8
import math

a = int(input('Digite um valor para o coeficiente A: '))
b = int(input('Digite um valor para o coeficiente B: '))
c = int(input('Digite um valor para o coeficiente C: '))

delta = b * b - 4 * a * c

if delta < 0:
    print 'A equação não possui raizes reais'
elif delta == 0:
    raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
    print 'A equação possui uma só raiz que é: ', raiz
elif delta > 0:
    raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)
    print 'As raizes da equação são: ', raiz1, ' e ', raiz2