__author__ = 'gustavo'
#coding:utf8

#Jogo de acerte o número

import os #Biclioteca de funcoes do sistema operacional
import random
random.seed()

valor = random.randint(1, 50)
chute = 0
tentativas = 0

os.system('clear')

while chute != valor:
    chute = int(input("Digite o seu palpite: "))
    tentativas = tentativas + 1

    if chute == valor:
        print 'Parabéns. Você acertou em ',  tentativas ," tentativas!!!"

    elif chute < valor:
        print 'Errou para menos na tentativa ', tentativas

    else:
        print 'Errou para mais tentativas ', tentativas




