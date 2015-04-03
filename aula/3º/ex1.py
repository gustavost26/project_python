__author__ = 'gustavo'
#coding:utf8

# x = 0
#
# while x <= 1000:
#     print x
#     x = x + 1

# contador = 0
#
# while contador <= 1000:
#     print contador
#     contador = contador + 2



contador   = 0
acumulador = 0

quantidade = int(input('Digite a quantidade de vezes a ser utilizado: '))

while contador < quantidade:
    numero = int(input('Digite um valor numerico: '))
    contador = contador + 1
    acumulador = acumulador + numero
    print 'A soma total dos numeros acumulados é: ', acumulador


