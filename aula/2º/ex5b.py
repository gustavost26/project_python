__author__ = 'gustavo'
#coding:utf8


a = int(input('Digite o valor para A: '))
b = int(input('Digite o valor para B: '))
c = int(input('Digite o valor para C: '))

if a > b and a > c:
    print 'A é maior que B e C'
elif b > a and b > c:
    print 'B é maior que A e C'
else:
    print 'C é maior que A e B'